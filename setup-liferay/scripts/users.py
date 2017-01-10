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

        if 'bibboxadmin' not in screenNames:
            print("CREATE BIBBOX VM ADMIN USER")

            param =  {
                "companyId":  self.companyId,
                "autoPassword": False,
                "password1": self.defaultPassword,
                "password2": self.defaultPassword,
                "autoScreenName": False,
                "screenName": "bibboxadmin",
                "emailAddress": "bibboxadmin@bibbox.org",
                "facebookId": 0,
                "openId": "",
                "locale": "en_US",
                "firstName": "Roxana",
                "middleName": "",
                "lastName": "Rilling",
                "prefixId": 0,
                "suffixId": 0,
                "male": False,
                "birthdayMonth": 1,
                "birthdayDay": 1,
                "birthdayYear": 1970,
                "jobTitle": "BIBBOX VM and LIFERAY Admin",
                "groupIds": None,
                "organizationIds": None,
                "roleIds": [roleIds['BIBBOX VM Admin'], roleIds['Administrator']],
                "userGroupIds": None,
                "sendEmail": False,
                "serviceContext": {"assetTagNames": ["bibboxadmin"]}
            }
            r = api.call("/user/add-user", param )
            user =  json.loads(r.text)
            
            bibboxadminpic = dir + '/avatar-pics/roxana.jpg'
            
            with open(bibboxadminpic, 'rb') as f:
                picdata = f.read()

            param = {
                "userId": user['userId'],
                "bytes": list(picdata),
            }
            r = api.call("/user/update-portrait", param)


        if 'admin' not in screenNames:
            print("CREATE BIBBOX ADMIN USER")

            param = {
                "companyId": self.companyId,
                "autoPassword": False,
                "password1": self.defaultPassword,
                "password2": self.defaultPassword,
                "autoScreenName": False,
                "screenName": "admin",
                "emailAddress": "admin@bibbox.org",
                "facebookId": 0,
                "openId": "",
                "locale": "en_US",
                "firstName": "Alan",
                "middleName": "",
                "lastName": "Punter",
                "prefixId": 0,
                "suffixId": 0,
                "male": True,
                "birthdayMonth": 1,
                "birthdayDay": 1,
                "birthdayYear": 1970,
                "jobTitle": "BIBBOX Admin",
                "groupIds": None,
                "organizationIds": None,
                "roleIds": roleIds['BIBBOX Admin'],
                "userGroupIds": None,
                "sendEmail": False,
                "serviceContext": {"assetTagNames": ["admin"]}
            }

            r = api.call("/user/add-user", param)

            user = json.loads(r.text)
            
            adminpic = dir + '/avatar-pics/alan.jpg'
            
            with open(adminpic, 'rb') as f:
                picdata = f.read()

            param = {
                "userId": user['userId'],
                "bytes": list(picdata),
            }
            r = api.call("/user/update-portrait", param)

        if 'pi' not in screenNames:
                print("CREATE BIBBOX PI USER")

                param = {
                    "companyId": self.companyId,
                    "autoPassword": False,
                    "password1": self.defaultPassword,
                    "password2": self.defaultPassword,
                    "autoScreenName": False,
                    "screenName": "pi",
                    "emailAddress": "pi@bibbox.org",
                    "facebookId": 0,
                    "openId": "",
                    "locale": "en_US",
                    "firstName": "Majmuna",
                    "middleName": "",
                    "lastName": "Sandu",
                    "prefixId": 0,
                    "suffixId": 0,
                    "male": False,
                    "birthdayMonth": 1,
                    "birthdayDay": 1,
                    "birthdayYear": 1970,
                    "jobTitle": "BIBBOX PI",
                    "groupIds": None,
                    "organizationIds": None,
                    "roleIds": roleIds['BIBBOX PI'],
                    "userGroupIds": None,
                    "sendEmail": False,
                    "serviceContext": {"assetTagNames": ["admin"]}
                }
                r = api.call("/user/add-user", param)
                user = json.loads(r.text)
                
                pipic = dir + '/avatar-pics/maimuna.png'
                
                with open(pipic, 'rb') as f:
                    picdata = f.read()

                param = {
                    "userId": user['userId'],
                    "bytes": list(picdata),
                }
                r = api.call("/user/update-portrait", param)


        if 'curator' not in screenNames:
                print("CREATE BIBBOX CURATOR USER")

                param = {
                    "companyId": self.companyId,
                    "autoPassword": False,
                    "password1": self.defaultPassword,
                    "password2": self.defaultPassword,
                    "autoScreenName": False,
                    "screenName": "curator",
                    "emailAddress": "curator@bibbox.org",
                    "facebookId": 0,
                    "openId": "",
                    "locale": "en_US",
                    "firstName": "Santa",
                    "middleName": "",
                    "lastName": "Morello",
                    "prefixId": 0,
                    "suffixId": 0,
                    "male": False,
                    "birthdayMonth": 1,
                    "birthdayDay": 1,
                    "birthdayYear": 1970,
                    "jobTitle": "BIBBOX Curator",
                    "groupIds": None,
                    "organizationIds": None,
                    "roleIds": roleIds['BIBBOX Curator'],
                    "userGroupIds": None,
                    "sendEmail": False,
                    "serviceContext": {"assetTagNames": ["curator"]}
                }
                r = api.call("/user/add-user", param)
                user = json.loads(r.text)

                curatorpic = dir + '/avatar-pics/santa.png'
                
                with open(curatorpic, 'rb') as f:
                    picdata = f.read()

                param = {
                    "userId": user['userId'],
                    "bytes": list(picdata),
                }
                r = api.call("/user/update-portrait", param)

        if 'operator' not in screenNames:
            print("CREATE BIBBOX PI USER")

            param = {
                "companyId": self.companyId,
                "autoPassword": False,
                "password1": self.defaultPassword,
                "password2": self.defaultPassword,
                "autoScreenName": False,
                "screenName": "operator",
                "emailAddress": "operator@bibbox.org",
                "facebookId": 0,
                "openId": "",
                "locale": "en_US",
                "firstName": "Carmen",
                "middleName": "",
                "lastName": "Thatcher",
                "prefixId": 0,
                "suffixId": 0,
                "male": False,
                "birthdayMonth": 1,
                "birthdayDay": 1,
                "birthdayYear": 1970,
                "jobTitle": "BIBBOX Operator",
                "groupIds": None,
                "organizationIds": None,
                "roleIds": roleIds['BIBBOX Operator'],
                "userGroupIds": None,
                "sendEmail": False,
                "serviceContext": {"assetTagNames": ["operator"]}
            }
            r = api.call("/user/add-user", param)
            user = json.loads(r.text)
            
            operatorpic = dir + '/avatar-pics/carmen.jpg'
            
            with open(operatorpic, 'rb') as f:
                picdata = f.read()

            param = {
                "userId": user['userId'],
                "bytes": list(picdata),
            }
            r = api.call("/user/update-portrait", param)
