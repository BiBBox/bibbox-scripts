#!/usr/bin/env python

import os
import sys
import getopt
import json
from pprint import pprint

def updatePorts(template, portmap):
    for portname in portmap.keys():
        if(portname.startswith("§§")):
            template = template.replace(portname, portmap[portname])
        elif(portname == "instance"):
            template = template.replace("§§INSTANCE", portmap[portname])
    return template

def updateParameters(template, environment):
    for var in environment.keys():
        template = template.replace(var, environment[var])
    return template

def updateEnvironment(template, environment):
    for var in environment.keys():
        template = template.replace(var, environment[var])
    return template

print ("SETUP UP DOCKER-COMPOSE")

argv = sys.argv[1:]
opts, args = getopt.getopt(argv,"a:i:",["applicationpath=","instancepath="])
for opt, arg in opts:
    if opt == '-h':
        print('test.py -a <applicationpath> -i <instancepath>')
        sys.exit()
    elif opt in ("-a", "--applicationpath"):
        applicationpath = arg
    elif opt in ("-i", "--instancepath"):
        instancepath = arg

template = open(instancepath + '/docker-compose-template.yml', 'r').read()

with open(instancepath + "/portmap.json") as data_file:
    portmap = json.load(data_file)
template = updatePorts(template, portmap)

with open(instancepath + "/environment-parameters-settings.json") as data_file:
    environment = json.load(data_file)
template = updateParameters(template, environment)

with open(instancepath + "/config-parameters-settings.json") as data_file:
    config = json.load(data_file)
template = updateParameters(template, environment)

target = open(instancepath + "/docker-compose.yml", 'w')
target.write(template)
target.close()