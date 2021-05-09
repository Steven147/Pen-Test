#将awvs.py生成的报告中高危漏洞的名称进行存储
import json

def store_vulner(filename):
    filename = "../vuln.json"
    allvulners = []
    vuln_count=0
    with open(filename) as f:
        vuln_list = json.load(f)
    for vuln_dict in vuln_list:
        if vuln_dict['severity'] >= 3:
            allvulners.append(vuln_dict['vt_name'])
            vuln_count = vuln_count+1
    print(vuln_count)
    return allvulners

a = store_vulner("../vuln.json")
for b in a:
    print(b)