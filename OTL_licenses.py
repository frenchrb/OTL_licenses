#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv
import sys
import re

def main(input, output):
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    browser = webdriver.Firefox(capabilities=firefox_capabilities)    
    outputFile = open(output, 'w')
    writer = csv.writer(outputFile, doublequote=True, escapechar='\\', lineterminator='\r')

    with open(input, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            result = row
            if 'http' not in row[len(row)-1]:
                result.append('LICENSE')
                result.append('540FIELD')
                writer.writerow(result)
            else:
                url = row[len(row)-1]
                browser.get(url)
                license = browser.find_element_by_class_name(
                    'Badge-Condition').text
                license = str.replace(license, u'\n', ' :: ')
                license = str.replace(license, u'\r', ' :: ')
                result.append(license)
                
                if "Attribution-NonCommercial-ShareAlike :: CC BY-NC-SA" in license:
                    field506 = "This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) License.$uhttps://creativecommons.org/licenses/by-nc-sa/4.0/legalcode"
                elif "Attribution-NonCommercial-NoDerivs :: CC BY-NC-ND" in license:
                    field506 = "This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs (CC BY-NC-ND) License.$uhttps://creativecommons.org/licenses/by-nc-nd/4.0/legalcode"
                elif "Attribution-NonCommercial :: CC BY-NC" in license:
                    field506 = "This work is licensed under a Creative Commons Attribution-NonCommercial (CC BY-NC) License.$uhttps://creativecommons.org/licenses/by-nc/4.0/legalcode"
                elif "Attribution-NoDerivs :: CC BY-ND" in license:
                    field506 = "This work is licensed under a Creative Commons Attribution-NoDerivs (CC BY-ND) License.$uhttps://creativecommons.org/licenses/by-nd/4.0/legalcode"
                elif "Attribution-ShareAlike :: CC BY-SA" in license:
                    field506 = "This work is licensed under a Creative Commons Attribution-ShareAlike (CC BY-SA) License.$uhttps://creativecommons.org/licenses/by-sa/4.0/legalcode"
                elif "Attribution :: CC BY" in license:
                    field506 = "This work is licensed under a Creative Commons Attribution (CC BY) License.$uhttps://creativecommons.org/licenses/by/4.0/legalcode"
                elif "Free Documentation License :: GNU" in license:
                    field506 = "This work is licensed under a GNU Free Documentation License.$uhttp://www.gnu.org/licenses/fdl.html"
                else:
                    field506 = ""
                result.append(field506)
                writer.writerow(result)

    browser.close()
    outputFile.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])