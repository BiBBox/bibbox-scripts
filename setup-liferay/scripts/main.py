#!/usr/bin/env python

import json
import urllib
import time

import requests
import jsonws


import sites
import roles
import users

print ("SETUP SCRIPT FOT eB3KIT BIBBOX DEMO")

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
        print("Connection try:" + counter + "| Server still starting up, connection Timed out.")
        if(counter > 10):
            return
        time.sleep(15)
        testServerStarted(counter + 1)
    except requests.exceptions.TooManyRedirects:
        print("Error to many Redirects")
        # Tell the user their URL was bad and try a different one
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)
        print("Connection try:" + counter + "| Error connecting to API.")
        if (counter > 10):
            return
        time.sleep(15)
        testServerStarted(counter + 1)

print("Trying to connect to liferay server.")
testServerStarted(0)

print ("SETUP SITES")
siteService = sites.Sites(companyId = '20116')
siteService.initSites()

print ("SETUP USERS")
userService = users.Users (companyId = '20116')
userService.initUsers()

api = jsonws.API()
