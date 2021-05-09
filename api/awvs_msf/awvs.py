import requests
import  json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class awvs(object):
    def __init__(self):
        self.task = []
        self.server = 'https://127.0.0.1:13443/api/v1/'
        self.apikey = '1986ad8c0a5b3df4d7028d5f3c06e936c0649ed47727e46cf96209680608d692d'
        self.headers = {
            'X-Auth': self.apikey,
            'Content-type': 'application/json'
        }
        self.scan_rule = {
            "FS" : "11111111-1111-1111-1111-111111111111", #完全扫描
            "HR" : "11111111-1111-1111-1111-111111111112", #高风险漏洞扫描
            "XSS": "11111111-1111-1111-1111-111111111116", #XSS漏洞
            "SQL": "11111111-1111-1111-1111-111111111113", #SQL注入
            "WP" : "11111111-1111-1111-1111-111111111115", #弱口令检测
            "CO" : "11111111-1111-1111-1111-111111111117", #Crawl Only
            "MS" : "11111111-1111-1111-1111-111111111120"  #恶意软件扫描
        }
        self.W = '\033[0m'
        self.G = '\033[1;32m'
        self.O = '\033[1;33m'
        self.R = '\033[1;31m'
        self.B = '\033[1;34m'
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.tid = ''
        self.sid = ''
    
    def scan_type(self):
        try:
            l = '[0] Full Scan\n'
            l += '[1] High Risk Vulnerabilities\n'
            l += '[2] Cross-site Scripting Vulnerabilities\n'
            l += '[3] SQL Injection Vulnerabilities\n'
            l += '[4] Weak Passwords\n'
            l += '[5] Crawl Only\n'
            l += '[6] Malware Scan'
            print (self.G+l+self.W)
            rule = input(self.O+'[Awvs_Api/Set_Rule]>> '+self.W)
            if rule == '0':
                return self.scan_rule['FS']
            elif rule == '1':
                return self.scan_rule['HR']
            elif rule == '2':
                return self.scan_rule['XSS']
            elif rule == '3':
                return self.scan_rule['SQL']
            elif rule == '4':
                return self.scan_rule['WP']
            elif rule == '5':
                return self.scan_rule['CO']
            else:
                print (self.R+'[-] Ops, 输入有误...'+self.W)
        except Exception as e:
            pass

    def request(self,path):
        try:
            return requests.get(url = self.server+path, timeout = 10, headers = self.headers, 
            verify = False)
        except Exception as e:
            print(e)
    
    def add(self):#添加扫描对象
        try:
            target = input(self.O+'[Awvs_Api/Set_Target]>> '+self.W)
            data ={
                "address":target,
                "description":"叶鸿宇",
                "criticality":"10"
            }
            r = requests.post(url = self.server+'targets', timeout = 10,
            verify = False, headers = self.headers, data=json.dumps(data))
            r_json = r.json()
            if r.status_code == 201:
                tid = r_json['target_id']
                self.tid  = tid
                print('tid: '+self.tid)
                return tid
        except Exception as e:
            print(e)
    
    def scan(self):#建立扫描任务
        try:
            data = {
                "target_id": self.add(),
                "profile_id":self.scan_type(),
                "schedule":    
                    {"disable": False,
                    "start_date":None,
                    "time_sensitive":False
                    }
            }
            r = requests.post(url = self.server+'scans', timeout = 10, verify  = False,
            headers  = self.headers, data = json.dumps(data))
            time.sleep(1)
            self.scan_id()
            if r.status_code == 201:
                print (self.G+'[-] OK, 扫描任务已经启动...'+self.W)
                self.scan_state()
        except Exception as e:
            print(e)
    
    def scan_id(self):#获取scan_id
        try:
            print('tid: '+self.tid)
            scan_url = self.server+'scans?l=20&q=target_id:' + self.tid
            r = requests.get(url = scan_url, 
            headers = self.headers, verify = False)
            r_json =  r.json()
            self.sid = r_json['scans'][0]['scan_id']
            #self.jprint(r.json())
            print('scan_id: '+self.sid)
        except Exception as e:
            print(e)
    
    def jprint(self,obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def scan_state(self):
        try:
            r = requests.get(url = self.server+'scans/'+self.sid, 
            headers = self.headers, verify = False)
            r_json = r.json()
            scan_state = r_json['current_session']['status']
            print('扫描状态: '+scan_state)
            while    scan_state != 'completed' and scan_state != 'aborted' :
                state = requests.get(url = self.server+'scans/'+self.sid , headers = self.headers
                 , verify = False)
                state_json = state.json()
                scan_state = state_json['current_session']['status']   
                time.sleep(10)
                print('扫描状态: '+ scan_state )
            print ('扫描结束')
        except Exception as e:
            print(e)
    
    def report(self):
        try:
            data = {"template_id":"11111111-1111-1111-1111-111111111112",
            "source":{
                 "list_type":"scans",
                "id_list":[self.sid]
                }
            }
            r = requests.post(url = self.server+'reports', headers = self.headers, 
            verify = False, data = json.dumps(data))
            print('报告生成中...............')
            time.sleep(10)
            if r.status_code == 201:
                self.download()    
        except Exception as e:
            print(e)
    
    def download(self):
        try:
            r = requests.get(url = self.server+'reports', headers = self.headers,
            verify = False)
            r_json = r.json()
            d_url = r_json['reports'][0]['download'][0]
            d_url = "https://127.0.0.1:13443"  + d_url
            d = requests.get(url = d_url, headers = self.headers , verify =False)
            with open(r"/root/桌面/report.html", "wb") as f:
                f.write(d.content)
            print("报告下载成功")
        except Exception as e:
            print(e)
    
    def vuln(self):
        try:
            vuln_url = self.server+'vulnerabilities?q=status:open'
            vuln = requests.get(url =  vuln_url, headers = self.headers, verify = False)
            #self.jprint(vuln.json())
            vuln_json = vuln.json()
            cursor = vuln_json['pagination']['next_cursor']
            print(cursor)
            vuln_url = self.server+'vulnerabilities?c='+cursor+'&q=status:open'
            vuln2 = requests.get(url =  vuln_url, headers = self.headers, verify = False)
            #self.jprint(vuln2.json())
            vuln_json2 = vuln2.json()
            cursor = vuln_json['pagination']['next_cursor']
            print(cursor)
            vulner  = vuln_json['vulnerabilities']
            vulner2  = vuln_json2['vulnerabilities']
            vulner.extend(vulner2)
            vulners = json.dumps(vulner, sort_keys=True, indent=4)
            vulnerb = vulners.encode('utf-8')
            with open(r"/root/桌面/vuln.json","wb") as f:
                f.write(vulnerb)
            print("漏洞信息下载成功")
        except Exception as e:
            print(e)

    def delete(self):
        try:
            del_url = self.server+'targets/'+self.tid
            dele = requests.delete(url = del_url, headers = self.headers, verify = False)
            print("删除成功")
        except Exception as e:
            print(e)

    def handle(self):
        try:
            self.usage()
            print('*'*40)
            while True:
                show = input(self.O+'[Awvs_Api]>> '+self.W)
                if show == 'scan':
                    self.scan()
                elif show == 'report':
                    self.report()
                elif show == 'vuln':
                    self.vuln()
                elif show == 'delete':
                    self.delete()
                elif show == 'exit':
                    break
                elif show == '':
                    pass
                else:
                    print (self.R+'[-] Ops, 输入错误...'+self.W)
        except KeyboardInterrupt:
            pass
    
    def usage(self): 
        s = '帮助:\n'
        s += '    scan     开始扫描任务\n'
        s += '    report   任务扫描报告\n'
        s += '    vuln     导出漏洞信息\n'
        s += '    delete   删除扫描任务\n'
        s += '    exit     退出扫描任务'
        print (self.B+s+self.W)

if __name__ == '__main__':
    awvs = awvs()
    awvs.handle()