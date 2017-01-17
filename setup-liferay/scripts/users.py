import json
import urllib

import requests
import jsonws
import roles
import os

class Users:

    def __init__(self, companyId=0):

        print ("WELCOME IN USER SERVICE")
        self.allUsers= {}
        self.companyId = companyId
        self.defaultPassword = "graz2017"


        api = jsonws.API()
        r = api.call("/user/get-company-users", {'companyId': self.companyId, 'start':"0", 'end':'1000'})
        users = json.loads(r.text)
        for ux in users:
            self.allUsers[ux['screenName']] = ux['userId']
        print (self.allUsers)

    def userIds (self):
        return self.allUsers

    def description(self, screenName):
        api = jsonws.API()
        return api.call("/user/get-user-by-screen-name", {'companyId': self.companyId, 'screenName': screenName})


    def initUsers(self):

        api = jsonws.API()


        print("FIRST GENERATE THE ROLES")

        roleService = roles.Roles(companyId=self.companyId )
        roleService.initRoles()
        roleIds = roleService.rolesIds()

        screenNames = self.allUsers.keys()
        
        dir = os.path.dirname(os.path.realpath(__file__))
        usersfile = dir + '/config/users.json'
        
        # Load User configurations
        with open(usersfile) as data_file:
            data = json.load(data_file)
        #pprint(data)

        # Create all users that are not existing
        for user in data:
            if user["screenname"] not in screenNames:
                print("CREATE " + user["jobTitle"])

                rIDs = []

                for rID in user["roleIds"]:
                    rIDs.append(roleIds[rID])

                param =  {
                    "companyId":  self.companyId,
                    "autoPassword": False,
                    "password1": self.defaultPassword,
                    "password2": self.defaultPassword,
                    "autoScreenName": False,
                    "screenName": user["screenname"],
                    "emailAddress": user["emailAddress"],
                    "facebookId": 0,
                    "openId": "",
                    "locale": "en_US",
                    "firstName": user["firstName"],
                    "middleName": user["middleName"],
                    "lastName": user["lastName"],
                    "prefixId": 0,
                    "suffixId": 0,
                    "male": user["male"],
                    "birthdayMonth": user["birthdayMonth"],
                    "birthdayDay": user["birthdayDay"],
                    "birthdayYear": user["birthdayYear"],
                    "jobTitle": user["jobTitle"],
                    "groupIds": None,
                    "organizationIds": None,
                    "roleIds": rIDs,
                    "userGroupIds": None,
                    "sendEmail": False,
                    "serviceContext": user["serviceContext"]
                }
                r = api.call("/user/add-user", param)
                tmp_user =  json.loads(r.text)
                
                pic = dir + user["avatar"]
                
                with open(pic, 'rb') as f:
                    picdata = f.read()

                param = {
                    "userId": tmp_user['userId'],
                    "bytes": list(picdata),
                }
                r = api.call("/user/update-portrait", param)
