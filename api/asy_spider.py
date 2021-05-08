from asyncio import Queue, Event
from urllib.parse import urlparse, urljoin
from playwright._impl._page import Page
from playwright._impl._api_types import TimeoutError as TimeError
from playwright._impl._api_types import Error
from analysis import *
import asyncio
from playwright.async_api import async_playwright
import re
import json
import lxml.etree
import logging
import pickle

# import os
# os.putenv("DEBUG", "pw:api")
logger = logging.getLogger()

url_is_http = re.compile("http[s]?://", re.I)
ignore_static_files = re.compile(r"\.(mp4|ma3|pdf|avi|gif|png|jpeg|jpg|css|js|xlsx|docx|doc|pptx|json|xml)$")
reg_ip = re.compile(r"^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}(:\d{1,5})?$")
result = []

class BaseSpider:
    def __init__(self, browser, loop, tid, mode: str = "detect", ignore: str = "exit;logout", **kwargs):
        self.mode = mode
        self.browser = browser
        self.storage = ""
        self.content = None
        self.host = ""
        self.ignore = ignore.split(";")
        self.request_num = 0
        self.request_time = 0.0
        self.tid = tid
        self.username = 'admin'
        self.password = 'password'
        self.scan_domain = set()
        asyncio.set_event_loop(loop=loop)

    def get_host(self, url):
        ps = urlparse(url)
        self.host = ps.scheme + "://" + ps.netloc

    # save result
    async def response_log(self, response):
        print(f"获取数据{response.url}")
        result.append(response.url)

    def init_hook(self, page):
        page.on("dialog", self.handle_dialog)
        page.on("response", lambda response: self.response_log(response))

    async def async_init_hook(self, page):
        self.init_hook(page=page)

    async def new_page(self) -> Page:
        """
        :param origin: local storage的源
        :return:
        """
        if self.content is None:
            options = {"ignore_https_errors": True}
            self.content = await self.browser.new_context(**options)
        page = await self.content.new_page()
        page.set_default_navigation_timeout(5000)
        return page

    async def browser_open_url(self, page: Page, url: str):
        logger.info(f"[+] 请求地址 {url}")
        await page.goto(url=url)

    @staticmethod
    async def handle_dialog(dialog):
        await dialog.dismiss()

    @staticmethod
    async def sleep(timeout: float = 1.0):
        await asyncio.sleep(timeout)

    async def close_other_pages(self, first=1):
        """
            关闭多余的标签页
        :param first: 前几个
        :return:
        """
        for i in self.content.pages[first:]:
            await i.close()


class Spider(BaseSpider):
    def __init__(self, browser, loop, tid: str, ignore: str = "exit;logout", **kwargs):
        super(Spider, self).__init__(browser=browser, loop=loop, tid=tid, ignore=ignore, **kwargs)
        self.forms_set = []
        # self.verify = VerifyAnalysis()
        self.history_link = set()
        self.all_path = set()
        self.search_uri = Queue()
        self.event = Event()
        self.is_login = False
        # 扫描的域名范围
        self.cache_form = set()

    def set_event(self):
        self.event.set()

    @staticmethod
    def url_parse_rt_uri(url):
        u = urlparse(url)
        path = u.path
        if u.query != "":
            path = path + "?" + u.query
        if u.fragment == "":
            pass
        else:
            path = path + "#" + u.fragment.split("?", 1)[0]  # noqa
        return path, u

    async def get_url(self, url, page=None):
        """
            请求目标地址
        :param url: 目标地址
        :param page:
        :return:
        """
        logger.info("[+] 登录成功，进行下一步检测...")
        if page is None:
            page = await self.new_page()
        await self.browser_open_url(page=page, url=url)

    def choose_input_data(self, *args: str) -> (str, bool):  # noqa
        """
            选择输入框的数据
        :param args: 多个数据，代表input输入框内的文字
        :return:
        """
        for i in args:
            if is_username(i):
                return self.username, True
            elif is_password(i):
                return self.password, True
        return "admin", False

    async def _get_all_form(self, page: Page, retry=0):
        """
            获取所有的form表单，并自动登录
        """
        last_url = page.url
        login = False
        input_num = 0

        _input_user = await page.query_selector("text=/(用户名|密码|账号|手机号)/i")
        if _input_user is not None and await _input_user.is_hidden():
            body = await page.query_selector("body")
            html = await body.inner_html()
            # 判断是否存在跳转密码界面
            switch_passwd = is_switch_passwd_login(html)
            if len(switch_passwd) > 0 and not self.is_login:
                await page.click("text=密码登录")

        all_form = await page.query_selector_all("form")
        for index, f in enumerate(all_form):
            sub_f = {"name": [], "verify": False, "verify_url": [], "url": last_url, "method": "", "type": "common"}
            f_html = await f.evaluate("e => e.outerHTML")
            f_html_strip = re.sub(r'\s', '', f_html)
            all_input = await f.query_selector_all("xpath=//input|//textarea")
            if f_html_strip in self.cache_form:
                logger.info("[*] 跳过重复的表单")
                continue
            self.cache_form.add(f_html_strip)
            for i in all_input:
                # try:
                name = await i.get_attribute("name") or ''
                placeholder = await i.get_attribute("placeholder") or ''
                sub_f["name"].append(name)
                # except :
                #     logging.warning("[!] 页面已经刷新，获取DOM失败")
                #     return False
                i_html = await i.evaluate("e => e.outerHTML")
                ib = is_button(i_html)
                if ib:
                    ib = True
                    login = True
                if not await i.is_hidden() and not ib and not re.search(r'(clear|清空)', i_html, re.I):
                    if is_input_file(i_html):
                        logger.info("[*] 检测到文件上传接口，跳过")
                        break
                    try:
                        await i.hover(timeout=3000)
                        await i.click(timeout=3000)
                    except TimeError:
                        continue
                    if page.url != last_url:
                        await self.search_uri.put(page.url)
                        self.forms_set.append(sub_f)
                        return True

                    text = await i.text_content() or ''
                    if is_verify(name) or is_verify(placeholder) or is_verify(text):
                        sub_f.update({"verify": True})
                        sub_f["verify_url"] = [await i.get_attribute("src") or '' for i in
                                               await f.query_selector_all("img")]
                        for vi in sub_f["verify_url"]:
                            # data = self.socket.get_image(urlparse(vi).path)
                            # self.verify.read_memory_img(data)
                            # code = self.verify.auto_identify()
                            code = ""
                            if code == "":
                                continue
                            try:
                                await i.fill(code)
                                input_num += 1
                            except TimeError:
                                logger.error("[*] 输入超时，跳过")
                                continue
                        sub_f["type"] = "login"
                        login = True
                    else:
                        i_id = await i.get_attribute("id") or ''
                        i_type = await i.get_attribute("type") or ''
                        data, login = self.choose_input_data(placeholder, i_id, name, i_type)
                        try:
                            await i.fill(data, timeout=3000)
                            input_num += 1
                        except TimeError:
                            logger.error("[*] 输入超时，跳过")
                            continue
            self.forms_set.append(sub_f)
            if login and input_num > 0:
                button = await f.query_selector_all("text=登录")
                if not button:
                    button = await f.query_selector_all("button")
                try:
                    async with page.expect_navigation():
                        if len(button) > 0:
                            for b in button:
                                if get_login_button_text(await b.inner_text()) != '':
                                    await b.click()
                                    break
                        else:
                            button = await f.query_selector_all("xpath=//input[@type='submit']")
                            await button[-1].click(timeout=3000)
                except TimeError:
                    logger.error("[*] 点击超时，跳过")
                    break
                except:
                    logger.error("[+] 登录失败，提交失败...")
                    break
                # await self.sleep()
                # try:
                #     # 判断是否刷新
                #     await i.inner_html()
                # except:
                #     logging.warning("[!] 页面已经刷新，获取DOM失败")

                if last_url != page.url:
                    if index != len(all_form):
                        await self.search_uri.put(last_url)
                    ps = urlparse(page.url)
                    if ps.path.lstrip("/") not in self.history_link:
                        if login:
                            self.is_login = True
                        await self.search_uri.put(page.url)
                        self.history_link.add(ps.path.lstrip("/"))
                    try:
                        return await self.static_html_page_parse_all_path(page=page, form=False)
                    except Error as e:
                        logger.error("[!] 获取页面所有路径错误", exc_info=True)

                logger.info("[+] 登录成功，进行下一步检测...")
                return
        return

    async def get_all_path(self, page):
        ps, parse_url = self.url_parse_rt_uri(page.url)
        last_url = page.url
        await self.search_uri.put(ps)
        while self.search_uri.qsize() > 0:
            path: str = await self.search_uri.get()
            if url_is_http.match(path):
                path = self.url_parse_rt_uri(path)[0].lstrip("/")
            elif "../" in path:
                path = path.rsplit("../")[-1]
            if "/" == path:
                path = path.lstrip("/")
            path = path.lstrip("/")
            if path not in self.all_path and not ignore_static_files.search(path):
                if True in [True for i in self.ignore if i in path]:
                    continue
                if last_url != path:
                    last_url = path.lstrip("/")
                    if self.url_parse_rt_uri(page.url)[0].lstrip("/") != path:
                        try:
                            await self.browser_open_url(page=page,
                                                        url=f"{parse_url.scheme}://{parse_url.netloc}/{path}")
                        except TimeError:
                            logger.warning("[!] 页面请求超时")
                        except Error:
                            logger.error("[!] 请求错误", exc_info=True)
                            continue
                    try:
                        await self.static_html_page_parse_all_path(page)
                    except TimeError:
                        logger.warning("[!] 获取所有链接超时")
                    except Error:
                        logger.error("[!] 异常", exc_info=True)
                    self.all_path.add(path)
            await self.close_other_pages()
        logger.info("[+] 爬取完毕")

    async def static_html_page_parse_all_path(self, page: Page, form: bool = True):
        """
            获取页面所有的链接
        :param page: page实例
        :param form: 是否扫描表单
        :return:
        """
        is_js = re.compile(r"javascript:?", re.I)
        last_url = page.url
        last_ps = urlparse(last_url)

        # 点击ul li 标签
        try:
            all_li_list = await page.query_selector_all("xpath=//ul/li")
        except Exception as e:
            all_li_list = []
        for i in all_li_list:
            try:
                if not await i.query_selector("a") and await i.is_visible():
                    await i.click(timeout=2000)
            except Error:
                logger.warning("[*] 改版本不支持下拉框点选")
            except Exception:
                logger.error("[!] 点击 ul li错误", exc_info=True)

        html = await page.content()
        soup = lxml.etree.HTML(html)

        all_li_list = soup.xpath("//a")
        all_url = re.findall(r'=[\"\'](/\S+)(?=[\'\"][> ])', html)
        for i in all_url:
            if i not in self.history_link:
                await self.search_uri.put(i)
                self.history_link.add(i)

        # all_li_list = await page.query_selector_all("xpath=//ul/li/a")
        for i in all_li_list:
            # if self.event.is_set():
            #     logger.info(f"[+] {self.tid} 暂停扫描")
            #     self.event.clear()
            #     await self.event.wait()
            #     self.event.clear()
            link = i.get('href')
            # link = await i.get_attribute("href")
            if link == "#" or link is None or is_js.match(link):
                continue
            # if url_is_http.match(link) and urlparse(link).netloc != last_ps.netloc:
            if url_is_http.match(link):
                link_domain = urlparse(link).netloc
                if link_domain not in self.scan_domain and link_domain.split(":")[0] not in self.scan_domain:
                    logger.info(f"[*] 外链跳过 {link}")
                    # 若是外链 则不再请求
                    continue
            if "../" in link:
                link = urljoin(last_url, link)
            if link == ".":
                continue
            if not link.startswith("/"):
                if not url_is_http.match(link):
                    link = last_ps.path.rsplit("/", 1)[0] + "/" + link
            if link not in self.history_link:
                await self.search_uri.put(link)
                self.history_link.add(link)

        if form:
            try:
                await self._get_all_form(page=page)
            except Exception as e:
                logger.error(e)
            if page.url != last_url:
                await self.get_url(last_url, page=page)

    async def close(self):
        await self.content.close()


async def _spider(task_obj, target: str, **kwargs):
    page = await task_obj.new_page( )
    # page = await task_obj.new_page(origin=target)
    await task_obj.get_url(target, page=page)
    await task_obj.async_init_hook(page)
    await task_obj.get_url(target, page=page)
    await task_obj.get_all_path(page)
    await page.close()
    await task_obj.close()


async def run_spider(tid, target):
    loop = asyncio.get_event_loop()
    logger.info("[+] 启动爬虫中")
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=False)
        sp = Spider(browser=browser, loop=loop, tid=tid)
        return await _spider(task_obj=sp, target=target)


if __name__ == '__main__':
    # asyncio.run(run_spider('1', target='https://docs.python.org/zh-cn/3/'))
    asyncio.run(run_spider('1', target='https://demo.testfire.net/'))
    # asyncio.run(run_spider('1', target='http://10.10.10.133/phpMyAdmin/'))
    # asyncio.run(run_spider('1', target='http://10.10.10.133/dvwa'))
    # asyncio.run(run_spider('1', target='http://192.168.0.117/dvwa'))
    f=open('C:\\Users\\lshq9\\Documents\\GitHub\\Penetration-Testing\\api\\testfire.txt','wb')
    pickle.dump(result,f)
    f.close()
    print(result)