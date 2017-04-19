import re

hosts = open("/etc/hosts", 'r')
print(str(hosts.read()))
if re.search('255\.255\.255\.255(.*)localhost', str(hosts.read())):
    print('match')
else:
    print('nomatch')
    newhosts = ""
    linenumber = 0
    with open("/etc/hosts", 'r') as f:
        for line in f:
            newhosts += line
            if linenumber == 0:
                newhosts += "127.0.0.1 localhost\n"

    print(newhosts)