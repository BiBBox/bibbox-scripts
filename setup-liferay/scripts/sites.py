import json
import urllib
from pprint import pprint
import logging

import requests
import jsonws
import roles
import os

class Sites:

    def __init__(self, companyId=0, logger=""):

        self.allSites= {}
        self.companyId = companyId
        self.logger = logger

        self.logger.info("SETUP USERS \n")

        api = jsonws.API()
        r = api.call("/group/get-groups", {'companyId': self.companyId, 'parentGroupId': '0', 'site':'true'})
        #print(r.url)
        #print (r.text)
        groups = json.loads(r.text)
        for g in groups:
            if 'Guest'  in g['groupKey']:
                self.groupID = g['groupId']

        #print("GROUP ID = ", self.groupID )

        r = api.call("/layout/get-layouts", {'groupId': self.groupID, 'privateLayout': 'false'})
        self.logger.info("/layout/get-layouts")
        self.logger.info(r.text)
        #print (r.text)
        sites = json.loads(r.text)

        #print("SITES AVAILABLE")
        for si in sites:
            self.allSites[si['friendlyURL']] = si['layoutId']
        #print(self.allSites)


    def siteIDs (self):
        return self.allSites

    def initSites(self):
        # Get all friendlyURL alredy exits
        siteNames = self.allSites.keys()

        self.setTheme()

        dir = os.path.dirname(os.path.realpath(__file__))
        sitesfile = dir + '/config/sites.json'
        
        # Load Site configurations
        with open(sitesfile) as data_file:
            data = json.load(data_file)
        #pprint(data)

        # Create all sites that are not existing
        for site in data:
            if site["friendlyURL"] not in siteNames:
                print("Create " + site["friendlyURL"])
                self.createSite(site)

    def setTheme(self):
        api = jsonws.API()
        param = {'groupId': self.groupID,
                 'privateLayout': 'false',
                 'themeId': "bibbox_WAR_bibboxtheme",
                 'colorSchemeId': "",
                 'css': ""}

        r = api.call("/layoutset/update-look-and-feel", param)

    def createSite(self, sitejson):
        api = jsonws.API()

        roleService = roles.Roles(companyId=self.companyId)
        roleService.initRoles()
        roleIds = roleService.rolesIds()

        print("CREATE " + sitejson["name"] + " SITE")

        parentLayoutId = 0
        if(sitejson["parentSite"] != "0"):
            parentLayoutId = self.allSites[sitejson["parentSite"]]

        # Create Layout
        param = {'groupId' : self.groupID,
                'privateLayout' : 'false',
                'parentLayoutId': parentLayoutId,
                'name' : sitejson["name"],
                'title': sitejson["title"],
                'description': sitejson["description"],
                'type': 'portlet',
                'hidden' : sitejson["hidden"],
                'friendlyURL' : sitejson["friendlyURL"] }

        r = api.call ("/layout/add-layout", param)
        self.logger.info("/layout/add-layout")
        self.logger.info(r.text)

        site = json.loads(r.text)
        layoutID = site['layoutId']
        plid = site['plid']
        self.allSites[sitejson["friendlyURL"]] = layoutID

        # Update Layout setings, place Portlet
        param = {'groupId': self.groupID,
                 'privateLayout': 'false',
                 'layoutId': layoutID,
                 'typeSettings': sitejson["typeSettings"]}

        r = api.call("/layout/update-layout", param)
        self.logger.info("/layout/update-layout")
        self.logger.info(r.text)

        # Configure Portlet
        param = {
                'companyId': self.companyId,
                'plid': plid,
                'portletId': sitejson["portletId"],
                'preferences': sitejson["portletPreferences"]}
        print("self.companyId:" + self.companyId + " plid:" + plid + " portletId:" + sitejson["portletId"] + " preferences:" + sitejson["portletPreferences"])
        r = api.call("/BIBBOXDocker-portlet.set-portlet-configuration", param)

        self.logger.info("/BIBBOXDocker-portlet.set-portlet-configuration")
        self.logger.info(r.text)

        # Setup Permissions
        self.removePermission(plid, roleIds['Guest'], "VIEW")
        for permission in sitejson['permission']:
            for userrole in permission:
                for actionId in permission[userrole].split(","):
                    self.setPermission(plid, roleIds[userrole], actionId)


    def setPermission(self, plid, roleId, actionId):
        api = jsonws.API()
        param = {
            'companyId': self.companyId,
            'primKey': plid,
            'groupId': self.groupID,
            'name': 'com.liferay.portal.kernel.model.Layout',
            'roleId': roleId,
            'actionId': actionId,
            'scope': 4}

        r = api.call("/resourcepermission/add-resource-permission", param)
        self.logger.info("/resourcepermission/add-resource-permission")
        self.logger.info(r.text)

    def removePermission(self, plid, roleId, actionId):
        api = jsonws.API()
        param = {
            'companyId': self.companyId,
            'primKey': plid,
            'groupId': self.groupID,
            'name': 'com.liferay.portal.kernel.model.Layout',
            'roleId': roleId,
            'actionId': actionId,
            'scope': 4}

        r = api.call("/resourcepermission/remove-resource-permission", param)
        self.logger.info("/resourcepermission/remove-resource-permission")
        self.logger.info(r.text)
