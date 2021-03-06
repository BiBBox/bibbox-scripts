#!/usr/bin/env python

import os
import sys
import getopt
import shutil
import json
#import getpass

from pprint import pprint

def createFolders(instancepath, folder):
    directory = instancepath + "/" + folder
    print("Creating folders: " + directory)
    if not os.path.exists(directory):
        os.makedirs(directory)

    os.system("chmod -R 777 " +  instancepath + "/" + folder.split("/")[0])

def copyFiles(applicationpath, source, instancepath, destination):
    try:
        src = applicationpath + "/" + source
        dest = instancepath + "/" + destination
        if(os.path.isfile(src)):
            print("Copy file: " + destination)
            shutil.copy2(src, dest)
        if(os.path.isdir(src)):
            print("Copy folder: " + destination)
            shutil.copytree(src, dest)
    except:
        print("Unexpected copy error:" + str(sys.exc_info()[1]))

#print("Env thinks the user is [%s]" % (os.getlogin()));
#print("Effective user is [%s]" % (getpass.getuser()));


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

dir = os.path.dirname(os.path.realpath(__file__))
applicationfiles = os.path.join(dir, 'config/applicationfiles.json')

with open(applicationfiles) as data_file:
    applicationfiles_json = json.load(data_file)

with open(applicationpath + '/file_structure.json') as data_file:
    file_structure_json = json.load(data_file)

print("----------------")
for folder in file_structure_json["makefolders"]:
    createFolders(instancepath, folder)
    
print("----------------")
for folder in file_structure_json["copyfiles"]:
    copyFiles(applicationpath, folder['source'], instancepath, folder['destination'])

print("----------------")
for folder in applicationfiles_json["copyapplicationfiles"]:
    copyFiles(applicationpath, folder['source'], instancepath, folder['destination'])
  

# ASK ROBERT WHY THIS IS NOT WORKING HERE

#print("AFTER copyapplicationfiles ")
#os.system("ls -a ") 
#print("END OF ls -a")
    
#with open(instancepath + "/environment-parameters-settings.json") as data_file:
#    environment = json.load(data_file)
  
#for var in environment.keys():
#      print ("§§" + var, environment[var])
    