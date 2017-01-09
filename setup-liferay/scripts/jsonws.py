import requests
import json
import urllib
#
#   https://dev.liferay.com/develop/tutorials/-/knowledge_base/7-0/invoking-json-web-services
#
class API:

    def __init__(self):
        self.auth = ('test@liferay.com', 'test')
#        self.auth = ('bibboxadmin', 'bibbox2016')

    def call (self, command, param):

        invokeURL = "http://development.bibbox.org/api/jsonws/invoke"
        #invokeURL = "http://localhost:8080/api/jsonws/invoke"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        cmd = { command : param}
        return requests.post(invokeURL, data = json.dumps(cmd), auth=self.auth,  headers=headers)

