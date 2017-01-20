import os
import sys
import errno
import time
import requests

sys.stdout.write("SETUP SCRIPT FOR eB3KIT BIBBOX DEMO \n")

def testServerStarted(counter):
    try:
        auth = ('test', 'test')
        url = "http://localhost:8080/api/jsonws/BIBBOXDocker-portlet.get-updated-application-store-list"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

        r = requests.get(url, auth=auth, headers=headers)

        if(r.status_code != requests.codes.ok):
            print("Connection try:" + str(counter) + "| Bad API Response. " + str(r.status_code))
            if (counter > 60):
                sys.exit(errno.ETIME)
            time.sleep(30)
            testServerStarted(counter + 1)
    except requests.exceptions.Timeout:
        print("Connection try:" + str(counter) + "| Server still starting up, connection Timed out.")
        if(counter > 60):
            sys.exit(errno.ETIME)
        time.sleep(30)
        testServerStarted(counter + 1)
    except requests.exceptions.TooManyRedirects:
        sys.stderr.write("Error to many Redirects")
        # Tell the user their URL was bad and try a different one
    except requests.exceptions.RequestException as e:
        print(e)
        print("Connection try:" + str(counter) + "| Error connecting to API.")
        if (counter > 60):
            sys.exit(errno.ETIME)
        time.sleep(30)
        testServerStarted(counter + 1)

sys.stdout.write("Waiting for liferay server to start. \n")
testServerStarted(0)
