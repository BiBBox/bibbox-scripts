import json
import urllib

import requests
import jsonws

import roles

print ("SCRIPT STARTED")

roleService = roles.Roles(companyId = '20116')
roleService.initRoles()
roleIds = roleService.rolesIds()


for k in roleIds:
    print ("Role", k, "has ID", roleIds[k])

print ("=====  SET UP OF LIFERAY  ====")
print ("BIBBOX PI has role ID:",  roleIds['Bibbox PI'])


api = jsonws.API()

r = api.call("GET", "user/get-company-users", {'companyId':'20116', 'start':"0", 'end':'100'})

users = json.loads(r.text)
for u  in users:
    print (u['screenName'], "(" +  u['firstName'] +"," + u['lastName']+")", "has ID", u['userId'])

