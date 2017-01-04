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
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        cmd = { command : param}
        return requests.post(invokeURL, data = json.dumps(cmd), auth=self.auth,  headers=headers)



'''
FRIEDHOF
        apiURL = "http://development.bibbox.org/api/jsonws/" + command
#        apiURL = "http://demo.bibbox.org/api/jsonws/" + command
        l = len(param)
#        apiURL = apiURL + "." + str(l)
        apiURLShort = apiURL

        for k in param.keys():
            if param[k] == None:
                apiURL = apiURL + "/-" + k
            else:
                if type(param[k]) == dict:
                    apiURL = apiURL + "/" + k + "/" + urllib.parse.quote(json.dumps(param[k]), safe='')
                else:
                    apiURL = apiURL + "/" + k + "/" + urllib.parse.quote(param[k], safe='')
        print(apiURL)

        if method == 'GET':  return requests.get(apiURL, auth=self.auth)
        if method == 'POST': return requests.post(apiURL, auth=self.auth)

'''