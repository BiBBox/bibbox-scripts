import json
import urllib

import requests
import jsonws

import sites
import roles
import users

print ("SETUP SCRIPT FOT eB3KIT BIBBOX DEMO")

siteService = sites.Sites(companyId = '20116')
siteService.initSites()

userService = users.Users (companyId = '20116')
userService.initUsers()


#roleService = roles.Roles(companyId = '20116')
#roleService.initRoles()
#roleIds = roleService.rolesIds()


#for k in roleIds:
#    print ("Role", k, "has ID", roleIds[k])



api = jsonws.API()


# add to the user with screen nane 'admin' the roleID 'Bibbox Admin'
#
