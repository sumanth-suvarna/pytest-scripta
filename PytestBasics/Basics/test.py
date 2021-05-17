wlan_id = 10
dns_acl_list = ["DNS", "ACL", "List"]
commands = ["wireless wlan %s" % str(wlan_id)] + dns_acl_list + ["save"]
for cmd in commands:
    print(cmd)

commands = [f"wireless wlan f{wlan_id}"] + dns_acl_list + ["save"]
for cmd in commands:
    print(cmd)