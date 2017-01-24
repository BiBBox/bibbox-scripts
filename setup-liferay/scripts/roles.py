import json
import os
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

        dir = os.path.dirname(os.path.realpath(__file__))
        rolesfile = dir + '/config/roles.json'

        # Load Role configurations
        with open(rolesfile) as data_file:
            data = json.load(data_file)
        #pprint(data)

        # Create all roles that are not existing
        for role in data:
            if data["name"] not in roleNames:
                print("CREATE " + data["name"] + " ROLE")
                title = {'en_US': data["name"]}
                desc = {'en_US': data["description"]}

                param = {'className': 'com.liferay.portal.kernel.model.Role', 'classPk': '0', 'name': data["name"],
                         'titleMap': title, 'descriptionMap': desc, 'type': '1', 'subtype': None}

                r = api.call ("/role/add-role", param)
            

        r = api.call("/role/get-roles", {'companyId': self.companyId, 'types': '1'})
        self.allRoles = {}
        roles = json.loads(r.text)
        for rx in roles:
            self.allRoles [rx['name']] = rx['roleId']
