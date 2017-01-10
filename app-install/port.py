#!/usr/bin/env python

import json
from pprint import pprint

def creatVirtualHost(id, protocol, proxy, subdomain, instance, url, portnumber):
    print("Create VirtualHost for " + id)
    virtualhost = open('config/virtualhost_' + protocol.lower() + '.template', 'r').read()
    virtualhost = virtualhost.replace("subdomain", subdomain.replace('§§INSTANCE', str(instance)).lower())
    virtualhost = virtualhost.replace("url", str(url))
    virtualhost = virtualhost.replace("ip", "127.0.0.1")
    virtualhost = virtualhost.replace("port", str(portnumber))
    print(virtualhost)
    return virtualhost


print ("SETUP UP PORT")

with open('test/portinfo.json') as data_file:
    ports = json.load(data_file)
with open('test/portmap.json') as data_file:
    portsmapping = json.load(data_file)

pprint(ports)

baseurl = portsmapping['baseurl']
instance = portsmapping['instance']

virtualhost = ""

for port in ports['mappings']:
    virtualhost += creatVirtualHost(port['id'], port['protocol'], port['proxy'], port['url'], instance, baseurl, portsmapping[port['id']])

target = open("test/005-" + instance, 'w')
target.write(virtualhost)
target.close()


