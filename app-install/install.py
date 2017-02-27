#!/usr/bin/env python

import os
import re
import sys
import getopt
import json
from pprint import pprint

def updatePorts(template, portmap):
    for portname in portmap.keys():
        if(portname.startswith("§§")):
            template = template.replace(portname, str(portmap[portname]))
        elif(portname == "instance"):
            template = template.replace("§§INSTANCE", str(portmap[portname]))
    return template

def updateParameters(template, environment):
    for var in environment.keys():
        template = template.replace("§§" + var, str(environment[var]))
    return template

def testConfigMising(template):
    if(template.find("§§") != -1):
        print("ERROR: there are unchanged Variables in the compose file!!")
        m = re.search('(§§.+)[ :]?', template)
        if m:
            print("Found :" + m.group(1))
        sys.exit(os.EX_DATAERR)

print ("SETUP UP DOCKER-COMPOSE")

argv = sys.argv[1:]
opts, args = getopt.getopt(argv,"a:i:",["applicationpath=","instancepath="])
for opt, arg in opts:
    if opt == '-h':
        print('test.py -a <applicationpath> -i <instancepath>')
        sys.exit()
    elif opt in ("-a", "--applicationpath"):
        applicationpath = arg.strip()
    elif opt in ("-i", "--instancepath"):
        instancepath = arg.strip()

template = open(instancepath + '/docker-compose-template.yml', 'r').read()

with open(instancepath + "/portmap.json") as data_file:
    portmap = json.load(data_file)
template = updatePorts(template, portmap)

with open(instancepath + "/environment-parameters-settings.json") as data_file:
    environment = json.load(data_file)
template = updateParameters(template, environment)

with open(instancepath + "/config-parameters-settings.json") as data_file:
    config = json.load(data_file)
template = updateParameters(template, config)

testConfigMising(template)

target = open(instancepath + "/docker-compose.yml", 'w')
target.write(template)
target.close()

#
# REPLACE ENVIRONMENT VARIABLES IN OTHER FILES
#

with open(applicationpath + '/file_structure.json') as data_file:
    file_structure_json = json.load(data_file)

if "configs-to-adapt" in file_structure_json:

    for filename in file_structure_json["configs-to-adapt"]:
        print("REPLACE ENVIRONMENT in ", filename)
        source = open(instancepath + '/'+ filename, 'r');
        origdata = source.read()
        source.close()
 
        replaced_data = updateParameters(origdata,      environment)
        replaced_data = updateParameters(replaced_data, config)
    
#    print("replaced = ", replaced_data )
        target = open(instancepath + '/'+ filename, 'w');
        target.write(replaced_data)
        target.close()

