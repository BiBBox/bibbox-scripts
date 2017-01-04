import json
import urllib

import requests
import jsonws
import roles

class Users:

    def __init__(self, companyId=0):

        print ("WELCOME IN USER SERVICE")
        self.allUsers= {}
        self.companyId = companyId

        api = jsonws.API()
        r = api.call("GET", "user/get-company-users", {'companyId': self.companyId, 'start':"0", 'end':'1000'})
        users = json.loads(r.text)
        for ux in users:
            self.allUsers[ux['screenName']] = ux['userId']
        print (self.allUsers)

    def userIds (self):
        return self.allUsers

    def description(self, screenName):
        api = jsonws.API()
        return api.call("GET", "user/get-user-by-screen-name", {'companyId': self.companyId, 'screenName': screenName})


    def initUsers(self):
        api = jsonws.API()

        roleService = roles.Roles(companyId='20116')
        roleService.initRoles()
        roleIds = roleService.rolesIds()

        screenNames = self.allUsers.keys()

        if 'bibboxadmin' not in screenNames:
            print("CREATE BIBBOX VM ADMIN USER")


"""
        roleNames = self.allRoles.keys()

        if 'Bibbox Operator' not in roleNames:
            print("CREATE BIBBOX OPERATOR")
            title = {'en_US': 'Bibbox Operator'}
            desc = {
                'en_US': 'The BIBBOX operator role is intended for users with are operators of installed applications'}

            param = {'class-name': 'com.liferay.portal.kernel.model.Role', 'class-pk': '0', 'name': 'Bibbox Operator',
                     'title-map': title, 'description-map': desc, 'type': '1', 'subtype': None}

            r = api.call ("POST", "role/add-role", param)

            print(r.text)
#           operatorRole = json.loads(r.text)['roleId']
#           print(operatorRole)

        if 'Bibbox Admin' not in roleNames:
            print("CREATE BIBBOX ADMINISTRATOR")
            title = {'en_US': 'Bibbox Admin'}
            desc = {
                'en_US': 'The BIBBOX administrator role is intended for the admin, who can install, configure and delete applications.'}
            param = {'class-name': 'com.liferay.portal.kernel.model.Role', 'class-pk': '0', 'name': 'Bibbox Admin',
                     'title-map': title, 'description-map': desc, 'type': '1', 'subtype': None}
            r = api.call ("POST", "role/add-role", param)

 #           print(r.text)
 #           adminRole = json.loads(r.text)['roleId']
 #           print(adminRole)

        if 'Bibbox VM Admin' not in roleNames:
            print("CREATE BIBBOX VM ADMINISTRATOR")
            title = {'en_US': 'Bibbox VM Admin'}
            desc = {
                'en_US': 'The BIBBOX VM administrator role is intended for the administration of the virtual machine and liferay.'}
            param = {'class-name': 'com.liferay.portal.kernel.model.Role', 'class-pk': '0', 'name': 'Bibbox VM Admin',
                     'title-map': title, 'description-map': desc, 'type': '1', 'subtype': None}
            r = api.call ("POST", "role/add-role", param)
  #          print(r.text)
  #          vmadminRole = json.loads(r.text)['roleId']
  #          print(vmadminRole)

        if 'Bibbox PI' not in roleNames:
            print("CREATE BIBBOX PI")
            title = {'en_US': 'Bibbox PI'}
            desc = {'en_US': 'The BIBBOX PI role is intended for management of all application metadata.'}
            param = {'class-name': 'com.liferay.portal.kernel.model.Role', 'class-pk': '0', 'name': 'Bibbox PI',
                     'title-map': title, 'description-map': desc, 'type': '1', 'subtype': None}
            r = api.call ("POST", "role/add-role", param)
  #         print(r.text)
  #         piRole = json.loads(r.text)['roleId']
  #          print(piRole)

        if 'Bibbox Curator' not in roleNames:
            print("CREATE BIBBOX CURATOR")
            title = {'en_US': 'Bibbox Curator'}
            desc = {'en_US': 'The BIBBOX curator role is intended for management of all application metadata.'}
            param = {'class-name': 'com.liferay.portal.kernel.model.Role', 'class-pk': '0', 'name': 'Bibbox Curator',
                     'title-map': title, 'description-map': desc, 'type': '1', 'subtype': None}
            r = api.call("POST", "role/add-role", param)
#            print(r.text)
#            curatorRole = json.loads(r.text)['roleId']
#            print(curatorRole)

        r = api.call("GET", "role/get-roles", {'companyId': self.companyId, 'types': '1'})
        self.allRoles = {}
        roles = json.loads(r.text)
        for rx in roles:
            self.allRoles [rx['name']] = rx['roleId']
"""