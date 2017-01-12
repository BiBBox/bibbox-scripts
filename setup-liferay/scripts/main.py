#!/usr/bin/env python

import json
import urllib
import time
import os
import sys
import errno

import requests
import jsonws
from pprint import pprint

import sites
import roles
import users

sys.stdout.write("SETUP SCRIPT FOR eB3KIT BIBBOX DEMO \n")

def testServerStarted(counter):
    try:
        auth = ('test@liferay.com', 'test')
        url = "http://localhost:8080/api/jsonws/BIBBOXDocker-portlet.get-updated-application-store-list"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

        r = requests.get(url, auth=auth, headers=headers)

        if(r.status_code != requests.codes.ok):
            print("Connection try:" + str(counter) + "| Bad API Response. " + str(r.status_code))
            if (counter > 20):
                sys.exit(errno.ETIME)
            time.sleep(15)
            testServerStarted(counter + 1)
    except requests.exceptions.Timeout:
        print("Connection try:" + str(counter) + "| Server still starting up, connection Timed out.")
        if(counter > 20):
            sys.exit(errno.ETIME)
        time.sleep(15)
        testServerStarted(counter + 1)
    except requests.exceptions.TooManyRedirects:
        sys.stderr.write("Error to many Redirects")
        # Tell the user their URL was bad and try a different one
    except requests.exceptions.RequestException as e:
        print(e)
        print("Connection try:" + str(counter) + "| Error connecting to API.")
        if (counter > 20):
            sys.exit(errno.ETIME)
        time.sleep(15)
        testServerStarted(counter + 1)

sys.stdout.write("Trying to connect to liferay server. \n")
testServerStarted(0)

sys.stdout.write("SETUP SITES \n")
siteService = sites.Sites(companyId = '20116')
siteService.initSites()

sys.stdout.write("SETUP USERS \n")
userService = users.Users (companyId = '20116')
userService.initUsers()

api = jsonws.API()
