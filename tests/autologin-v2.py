# -*- coding: utf-8 -*-
"""
Created on Tue 4 Apr 2023

@author: Sridhar Machani
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

USERNAME = 'hero@swarajstudios.com'
PASSWORD = 'cL@P1dd$5xqQ0A'

BROWSERSTACK_URL = 'https://sridharmachani_cVTeOt:vEKxcBixzrsra51FAR2B@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
'bstack:options' : {
"os" : "macOS",
"osVersion" : "13",
"projectName" : "Sample sandbox project",
"buildName" : "Build #1",
"sessionName" : "My First Test",
},
"browserName" : "Chrome",
"browserVersion" : "latest",
}


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('"/Users/ssinc/Downloads/chromedriver_mac_arm64/chromedriver', chrome_options=options)
action = ActionChains(driver)
time.sleep(1)


driver.get('http://www.amazon.in')
time.sleep(3)
 
firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[2]')
action.move_to_element(firstLevelMenu).perform()
time.sleep(3)
 
secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(logindata.USERNAME)
time.sleep(3)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(logindata.PASSWORD)
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(3)
