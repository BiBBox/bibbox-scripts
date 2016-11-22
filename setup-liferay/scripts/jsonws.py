import requests
import json
import urllib
#
#   https://dev.liferay.com/develop/tutorials/-/knowledge_base/7-0/invoking-json-web-services
#
class API:

    def __init__(self):
        self.auth = ('bibboxadmin', 'bibbox2016')

    def call (self, method, command, param):
        apiURL = "http://demo.bibbox.org/api/jsonws/" + command
        l = len(param)
        apiURL = apiURL + "." + str(l)
        for k in param.keys():
            if param[k] == None:
                apiURL = apiURL + "/-" + k
            else:
                if type(param[k]) == dict:
                    apiURL = apiURL + "/" + k + "/" + urllib.parse.quote(json.dumps(param[k]))
                else:
                    apiURL = apiURL + "/" + k + "/" + urllib.parse.quote(param[k])
        print(apiURL)
        if method == 'GET':  return requests.get(apiURL, auth=self.auth)
        if method == 'POST': return requests.post(apiURL, auth=self.auth)