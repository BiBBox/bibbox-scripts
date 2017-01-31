import jsonws
import json
import os
import time
from datetime import datetime

class Journal:
    def __init__(self, companyId=0, groupID=0, logger=""):
        self.allJournalArticles = {}
        self.companyId = companyId
        self.groupID = groupID
        self.logger = logger

        self.logger.info("SETUP Journal Articles \n")

        api = jsonws.API()
        r = api.call("/journal.journalarticle/get-articles", {'groupId': self.groupID, 'folderId': '0'})
        print(r.text)
        articles = json.loads(r.text)
        for article in articles:
            print(article['urlTitle'])
            self.allJournalArticles[article['urlTitle']] = article['articleId'] # "id": "32402" or "resourcePrimKey": "32403" or "articleId": "32401",

        dir = os.path.dirname(os.path.realpath(__file__))
        journalsfile = dir + '/config/journal.json'

        # Load Site configurations
        with open(journalsfile) as data_file:
            self.data = json.load(data_file)

        self.journalsNames = self.allJournalArticles.keys()

    def journalArticleIDs(self):
        return self.allJournalArticles

    def createJournalArticle(self, articlename):
        journalarticle = self.data[articlename]
        if journalarticle["articleURL"] not in self.journalsNames:
            return self.createJournalArticlePrivate(journalarticle)
        else:
            return self.getArticleData(self.journalsNames[journalarticle["articleURL"]])

    def getArticleData(self, articleId):
        return ""

    def createJournalArticlePrivate(self, journalarticle):
        cdate = datetime.now()

        print(cdate)

        api = jsonws.API()
        print("Create " + journalarticle["articleURL"])
        r = api.call("/journal.journalarticle/add-article",
                     {'groupId': self.groupID,
                      'folderId': '0',
                      'classNameId': '0',
                      'classPK': '0',
                      'articleId': '',
                      'autoArticleId': 'true',
                      'titleMap': journalarticle["titleMap"],
                      'descriptionMap': '{}',
                      'content': journalarticle["content"],
                      'ddmStructureKey': 'BASIC-WEB-CONTENT',
                      'ddmTemplateKey': 'BASIC-WEB-CONTENT',
                      'layoutUuid': '',
                      'displayDateMonth': cdate.month-1,
                      'displayDateDay': cdate.day,
                      'displayDateYear': cdate.year-1,
                      'displayDateHour': cdate.hour,
                      'displayDateMinute': cdate.minute,
                      'expirationDateMonth': '0',
                      'expirationDateDay': '0',
                      'expirationDateYear': '0',
                      'expirationDateHour': '0',
                      'expirationDateMinute': '0',
                      'neverExpire': 'true',
                      'reviewDateMonth': '0',
                      'reviewDateDay': '0',
                      'reviewDateYear': '0',
                      'reviewDateHour': '0',
                      'reviewDateMinute': '0',
                      'neverReview': 'true',
                      'indexable': 'true',
                      'articleURL': journalarticle["articleURL"]
                      })
        print(r.text)
        article = json.loads(r.text)

        r2 = api.call("/assetentry/get-company-entries",
                     {'companyId': self.companyId,
                      'start': '-1',
                      'end': '-1'
                     })

        assets = json.loads(r2.text)
        print(r2.text)
        uuid = ""
        for asset in assets:
            if asset['classPK'] == article['resourcePrimKey']:
                print("Asset found for article")
                print("UUID: " + asset['classUuid'])
                uuid = asset['classUuid']


        template = "<portlet-preferences><preference><name>enableComments</name><value>false</value></preference><preference><name>enableRelatedAssets</name><value>true</value></preference><preference><name>subtypeFieldsFilterEnabled</name><value>false</value></preference><preference><name>enableViewCountIncrement</name><value>true</value></preference><preference><name>delta</name><value>20</value></preference><preference><name>showExtraInfo</name><value>true</value></preference><preference><name>showAvailableLocales</name><value>false</value></preference><preference><name>displayStyleGroupId</name><value>20147</value></preference><preference><name>assetLinkBehavior</name><value>showFullContent</value></preference><preference><name>selectionStyle</name><value>manual</value></preference><preference><name>displayStyle</name><value>full-content</value></preference><preference><name>enableSocialBookmarks</name><value>true</value></preference><preference><name>enablePermissions</name><value>true</value></preference><preference><name>enableRss</name><value>false</value></preference><preference><name>socialBookmarksDisplayStyle</name><value>menu</value></preference><preference><name>classNameIds</name></preference><preference><name>emailAssetEntryAddedEnabled</name><value>false</value></preference><preference><name>enableTagBasedNavigation</name><value>false</value></preference><preference><name>metadataFields</name><value></value></preference><preference><name>showContextLink</name><value>true</value></preference><preference><name>showQueryLogic</name><value>false</value></preference><preference><name>enableCommentRatings</name><value>false</value></preference><preference><name>emailFromAddress</name><value>noreply@bibbox.org</value></preference><preference><name>enableRatings</name><value>false</value></preference><preference><name>enablePrint</name><value>false</value></preference><preference><name>assetEntryXml</name><value>&lt;?xml version=&#34;§§version&#34;?&gt;[$NEW_LINE$][$NEW_LINE$]&lt;asset-entry&gt;[$NEW_LINE$]	&lt;asset-entry-type&gt;com.liferay.journal.model.JournalArticle&lt;/asset-entry-type&gt;[$NEW_LINE$]	&lt;asset-entry-uuid&gt;§§uuid&lt;/asset-entry-uuid&gt;[$NEW_LINE$]&lt;/asset-entry&gt;</value></preference><preference><name>socialBookmarksDisplayPosition</name><value>bottom</value></preference><preference><name>showAssetTitle</name><value>true</value></preference><preference><name>extensions</name></preference><preference><name>emailFromName</name><value>BIBBOX</value></preference><preference><name>paginationType</name><value>none</value></preference><preference><name>abstractLength</name><value>200</value></preference><preference><name>showMetadataDescriptions</name><value>true</value></preference><preference><name>enableFlags</name><value>false</value></preference><preference><name>showAddContentButton</name><value>true</value></preference></portlet-preferences>";
        template = template.replace("§§version", str(article["version"]))
        template = template.replace("§§uuid", str(uuid))

        return template