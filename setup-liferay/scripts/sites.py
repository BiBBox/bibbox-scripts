import json
import urllib

import requests
import jsonws

class Sites:

    def __init__(self, companyId=0):

        self.allSites= {}
        self.companyId = companyId

        api = jsonws.API()
        r = api.call("/group/get-groups", {'companyId': self.companyId, 'parentGroupId': '0', 'site':'true'})
        print(r.url)
        print (r.text)
        groups = json.loads(r.text)
        for g in groups:
            if 'Guest'  in g['groupKey']:
                self.groupID = g['groupId']

        print("GROUP ID = ", self.groupID )

        r = api.call("/layout/get-layouts", {'groupId': self.groupID, 'privateLayout': 'false'})
        print (r.text)
        sites = json.loads(r.text)

        print("SITES AVAILABLE")
        for si in sites:
            self.allSites[si['friendlyURL']] = si['layoutId']
        print(self.allSites)


    def siteIDs (self):
        return self.allSites


    def initSites(self):
        api = jsonws.API()

        siteNames = self.allSites.keys()

        if '/instances' not in siteNames:
            print("CREATE INSTANCES SITE")

            param = {'groupId' : self.groupID,
                     'privateLayout' : 'false',
                     'parentLayoutId': '0',
                     'name' : 'Applications',
                     'title': 'Applications',
                     'description': 'Applications',
                     'type': 'portlet',
                     'hidden' : 'false',
                     'friendlyURL' : '/instances' }

            r = api.call ("/layout/add-layout", param)
            site = json.loads(r.text)
            layoutID = site['layoutId']
            print("SITES GENERATED WITH", site['layoutId'])

            param = {'groupId': self.groupID,
                 'privateLayout': 'false',
                 'layoutId': layoutID,
                 'typeSettings': 'column-1=bibboxjscontainer_WAR_BIBBOXDockerportlet\nlayout-template-id=1_column'}

            r = api.call("/layout/update-layout", param)

            # set the correct permisions
