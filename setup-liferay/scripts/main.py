#!/usr/bin/env python

import json
import urllib
import time
import os
import sys
import errno
import logging

import requests
import jsonws
from pprint import pprint

import sites
import roles
import users
import journal

sys.stdout.write("SETUP SCRIPT FOR eB3KIT BIBBOX DEMO \n")
logger = logging.getLogger("app-analyser")

def setupLogger():
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('/opt/bibbox/setup-liferay.log')
    fh.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(fh)

def testServerStarted(counter):
    try:
        auth = ('test', 'test')
        url = "http://localhost:8080/api/jsonws/BIBBOXDocker-portlet.get-updated-application-store-list"
        #url = "http://dev2.bibbox.org/api/jsonws/BIBBOXDocker-portlet.get-updated-application-store-list"

        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

        r = requests.get(url, auth=auth, headers=headers)
        logger.info("Test: http://localhost:8080/api/jsonws/BIBBOXDocker-portlet.get-updated-application-store-list")
        logger.info(r.text)

        if(r.status_code != requests.codes.ok):
            print("Connection try:" + str(counter) + "| Bad API Response. " + str(r.status_code))
            logger.info("Connection try:" + str(counter) + "| Bad API Response. " + str(r.status_code))
            if (counter > 60):
                sys.exit(errno.ETIME)
            time.sleep(30)
            testServerStarted(counter + 1)
    except requests.exceptions.Timeout:
        print("Connection try:" + str(counter) + "| Server still starting up, connection Timed out.")
        logger.info("Connection try:" + str(counter) + "| Server still starting up, connection Timed out.")
        if(counter > 60):
            sys.exit(errno.ETIME)
        time.sleep(30)
        testServerStarted(counter + 1)
    except requests.exceptions.TooManyRedirects:
        sys.stderr.write("Error to many Redirects")
        logger.info("Error to many Redirects")
        # Tell the user their URL was bad and try a different one
    except requests.exceptions.RequestException as e:
        print(e)
        print("Connection try:" + str(counter) + "| Error connecting to API.")
        logger.info("Connection try:" + str(counter) + "| Error connecting to API.")
        if (counter > 60):
            sys.exit(errno.ETIME)
        time.sleep(30)
        testServerStarted(counter + 1)

def writeSetupDoneConfig():
    target = open("/etc/bibbox/conf.d/setup.cfg", 'w')
    target.write('setup="done"')
    target.close()

#setupLogger()

sys.stdout.write("Trying to connect to liferay server. \n")
logger.info("Trying to connect to liferay server. \n")
testServerStarted(0)

sys.stdout.write("SETUP SITES \n")
logger.info("SETUP SITES \n")
siteService = sites.Sites('20116', logger)
siteService.initSites()

sys.stdout.write("SETUP USERS \n")
logger.info("SETUP USERS \n")
userService = users.Users (companyId = '20116')
userService.initUsers()

#journalService = journal.Journal('20116', '20147', logger)
#journalService.initJournalArticles()

api = jsonws.API()

#writeSetupDoneConfig()

