import json
import urllib

import requests
import jsonws

class Roles:

    def __init__(self, companyId=0):
        self.allRoles = {}
        self.companyId = companyId
        api = jsonws.API()
        r = api.call("GET", "/role/get-roles", {'companyId': self.companyId, 'types': '1'})
#        print (r.text)
        roles = json.loads(r.text)
        for rx in roles:

            print (rx['uuid'])
            self.allRoles[rx['name']] = rx['roleId']
        print (self.allRoles)

    def rolesIds (self):
        return self.allRoles

    def description(self, roleId):
        api = jsonws.API()
        return api.call("GET", "/role/get-role", {'roleId': roleId})


    def initRoles(self):
        api = jsonws.API()
        roleNames = self.allRoles.keys()

        if 'Bibbox Operator' not in roleNames:
            print("CREATE BIBBOX OPERATOR")
            title = {'en_US': 'Bibbox Operator'}
            desc = {
                'en_US': 'The BIBBOX operator role is intended for users with are operators of installed applications'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'Bibbox Operator',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}

            r = api.call ("POST", "/role/add-role", param)

            print(r.text)
#           operatorRole = json.loads(r.text)['roleId']
#           print(operatorRole)

        if 'Bibbox Admin' not in roleNames:
            print("CREATE BIBBOX ADMINISTRATOR")
            title = {'en_US': 'Bibbox Admin'}
            desc = {
                'en_US': 'The BIBBOX administrator role is intended for the admin, who can install, configure and delete applications.'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'Bibbox Admin',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}

            r = api.call ("POST", "/role/add-role", param)

 #           print(r.text)
 #           adminRole = json.loads(r.text)['roleId']
 #           print(adminRole)

        if 'Bibbox VM Admin' not in roleNames:
            print("CREATE BIBBOX VM ADMINISTRATOR")
            title = {'en_US': 'Bibbox VM Admin'}
            desc = {
                'en_US': 'The BIBBOX VM administrator role is intended for the administration of the virtual machine and liferay.'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'Bibbox VM Admin',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}

            r = api.call ("POST", "/role/add-role", param)
  #          print(r.text)
  #          vmadminRole = json.loads(r.text)['roleId']
  #          print(vmadminRole)

        if 'Bibbox PI' not in roleNames:
            print("CREATE BIBBOX PI")
            title = {'en_US': 'Bibbox PI'}
            desc = {'en_US': 'The BIBBOX PI role is intended for management of all application metadata.'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'Bibbox PI',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}

            r = api.call ("POST", "/role/add-role", param)
  #         print(r.text)
  #         piRole = json.loads(r.text)['roleId']
  #          print(piRole)

        if 'Bibbox Curator' not in roleNames:
            print("CREATE BIBBOX CURATOR")
            title = {'en_US': 'Bibbox Curator'}
            desc = {'en_US': 'The BIBBOX curator role is intended for management of all application metadata.'}

            param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': 'Bibbox Curator',
                     'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}
            r = api.call("POST", "/role/add-role", param)
            
#            print(r.text)
#            curatorRole = json.loads(r.text)['roleId']
#            print(curatorRole)

        r = api.call("GET", "/role/get-roles", {'companyId': self.companyId, 'types': '1'})
        self.allRoles = {}
        roles = json.loads(r.text)
        for rx in roles:
            self.allRoles [rx['name']] = rx['roleId']
