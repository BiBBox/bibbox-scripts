import re
import os
import fileinput

class Setupchecker:
    def __init__(self, logger=""):
        self.logger = logger
        self.logger.info("Init Checks: \n")
        #self.checkVagrantError1()

    # VagrantError1
    # Error on Ubuntu host system with vagrant 1.8.x
    #
    # In the /ect/hosts file is the line for defining localhost not set,
    # with this liferay con not connect to the postgresql db
    def checkVagrantError1 (self):
        self.logger.info("Check Vagrant ERROR 1")
        hosts = open("/etc/hosts", 'w')
        if re.search('127\.0\.0\.1(.*)localhost', hosts.read()):
            self.logger.info(" - no error \n")
        else:
            self.logger.info(' - error found, fixing it \n')
            newhosts = ""
            linenumber = 0
            with open("/etc/hosts", 'r') as f1:
                for line in f1:
                    newhosts += line
                    if linenumber == 0:
                        newhosts += "127.0.0.1 localhost\n"
            hosts.write(newhosts)
            hosts.close()

            os.system("service liferay stop")
            os.system("service postgresql restart")
            os.system("service liferay start")