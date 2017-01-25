#!/usr/bin/env python

import os
import re
import time
import shutil

def stopLiferay():
    print("Stopping Liferay")
    os.system('service liferay stop')
    time.sleep(10)

def deleteLiferayFolders():
    shutil.rmtree('/opt/liferay/data/document_library')
    shutil.rmtree('/opt/liferay/data/elasticsearch')
    shutil.rmtree('/opt/liferay/tomcat-8.0.32/work/Catalina')
    for root, dirs, files in os.walk('/opt/liferay/tomcat-8.0.32/temp'):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))
    os.remove("/etc/bibbox/conf.d/setup.cfg")

def resetDB():
    os.system('./resetDB.sh')

print("Reset Liferay")
stopLiferay()
deleteLiferayFolders()
resetDB()
