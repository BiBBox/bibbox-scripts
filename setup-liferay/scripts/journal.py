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

    def journalArticleIDs(self):
        return self.allJournalArticles

    def initJournalArticles(self):
        journalsNames = self.allJournalArticles.keys()

        dir = os.path.dirname(os.path.realpath(__file__))
        journalsfile = dir + '/config/journal.json'

        # Load Site configurations
        with open(journalsfile) as data_file:
            data = json.load(data_file)

        for journalarticle in data:
            if journalarticle["articleURL"] not in journalsNames:
                self.createJournalArticle(journalarticle)

    def createJournalArticle(self, journalarticle):
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
                      'displayDateYear': cdate.year,
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