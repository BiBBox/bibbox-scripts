import json
import urllib
from pprint import pprint

import requests
import jsonws

class Roles:

    def __init__(self, companyId=0):
        self.allRoles = {}
        self.companyId = companyId
        api = jsonws.API()
        r = api.call("/role/get-roles", {'companyId': self.companyId, 'types': '1'})
#        print (r.text)
        roles = json.loads(r.text)
        for rx in roles:
            self.allRoles[rx['name']] = rx['roleId']
        print (self.allRoles)

    def rolesIds (self):
        return self.allRoles

    def description(self, roleId):
        api = jsonws.API()
        return api.call("/role/get-role", {'roleId': roleId})

    def initRoles(self):
        api = jsonws.API()
        roleNames = self.allRoles.keys()

        pprint(self.allRoles)


        if 'BIBBOX Admin' not in roleNames:
            print("CREATE BIBBOX ADMIN ROLE")
            title = {'en_US': 'BIBBOX Admin'}
            desc = {
                'en_US': 'The BIBBOX administrator role is intended for the admin, who can install, configure and delete applications.'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'BIBBOX Admin',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}

            r = api.call ("/role/add-role", param)

 #           print(r.text)
 #           adminRole = json.loads(r.text)['roleId']
 #           print(adminRole)

        if 'BIBBOX VM Admin' not in roleNames:
            print("CREATE BIBBOX VM ADMIN ROLE")
            title = {'en_US': 'BIBBOX VM Admin'}
            desc = {
                'en_US': 'The BIBBOX VM administrator role is intended for the administration of the virtual machine and liferay.'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'BIBBOX VM Admin',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}

            r = api.call ("/role/add-role", param)
  #          print(r.text)
  #          vmadminRole = json.loads(r.text)['roleId']
  #          print(vmadminRole)

        if 'BIBBOX PI' not in roleNames:
            print("CREATE BIBBOX PI ROLE")
            title = {'en_US': 'BIBBOX PI'}
            desc = {'en_US': 'The BIBBOX PI role is intended for management of all application metadata.'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'BIBBOX PI',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}

            r = api.call ("/role/add-role", param)
  #         print(r.text)
  #         piRole = json.loads(r.text)['roleId']
  #          print(piRole)

        if 'BIBBOX Curator' not in roleNames:
            print("CREATE BIBBOX CURATOR ROLE")
            title = {'en_US': 'BIBBOX Curator'}
            desc = {'en_US': 'The BIBBOX curator role is intended for management of all application metadata.'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'BIBBOX Curator',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}
            r = api.call("/role/add-role", param)
            
#            print(r.text)
#            curatorRole = json.loads(r.text)['roleId']
#            print(curatorRole)

        if 'BIBBOX Operator' not in roleNames:
            print("CREATE BIBBOX Operator ROLE")
            title = {'en_US': 'BIBBOX User'}
            desc = {'en_US': 'The BIBBOX curator role is intended for the operation of specific tools.'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'BIBBOX Operator',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}
            r = api.call("/role/add-role", param)

            #            print(r.text)
            #            curatorRole = json.loads(r.text)['roleId']
            #            print(curatorRole)

        r = api.call("/role/get-roles", {'companyId': self.companyId, 'types': '1'})
        self.allRoles = {}
        roles = json.loads(r.text)
        for rx in roles:
            self.allRoles [rx['name']] = rx['roleId']
