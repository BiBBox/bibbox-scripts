import re
import os
import fileinput

class Setupchecker:
    def __init__(self, logger=""):
        self.logger = logger
        self.logger.info("Init Checks: \n")