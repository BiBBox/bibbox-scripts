#!/usr/bin/env python

import json
import urllib
import time
import sys

import requests
import jsonws


import sites
import roles
import users

sys.stderr.write("SETUP SCRIPT FOT eB3KIT BIBBOX DEMO")

def testServerStarted(counter):
    try:
        auth = ('test@liferay.com', 'test')
        url = "http://localhost:8080/api/jsonws/BIBBOXDocker-portlet.get-updated-application-store-list"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

        r = requests.get(url, auth=auth, headers=headers)
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        sys.stderr.write("Connection try:" + counter + "| Server still starting up, connection Timed out.")
        if(counter > 10):
            return
        time.sleep(15)
        testServerStarted(counter + 1)
    except requests.exceptions.TooManyRedirects:
        sys.stderr.write("Error to many Redirects")
        # Tell the user their URL was bad and try a different one
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        sys.stderr.write(e)
        sys.stderr.write("Connection try:" + counter + "| Error connecting to API.")
        if (counter > 10):
            return
        time.sleep(15)
        testServerStarted(counter + 1)

sys.stderr.write("Trying to connect to liferay server.")
testServerStarted(0)

sys.stderr.write("SETUP SITES")
siteService = sites.Sites(companyId = '20116')
siteService.initSites()

sys.stderr.write("SETUP USERS")
userService = users.Users (companyId = '20116')
userService.initUsers()

api = jsonws.API()
