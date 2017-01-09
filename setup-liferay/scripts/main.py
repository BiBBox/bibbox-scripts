import json
import urllib

import requests
import jsonws

import sites
import roles
import users

print ("SETUP SCRIPT FOT eB3KIT BIBBOX DEMO")

print ("SETUP SITES")
siteService = sites.Sites(companyId = '20116')
siteService.initSites()

print ("SETUP USERS")
userService = users.Users (companyId = '20116')
userService.initUsers()

api = jsonws.API()
