#Import the web driver

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass


BROWSERSTACK_URL = 'https://sridharmachani_cVTeOt:vEKxcBixzrsra51FAR2B@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
'bstack:options' : {
"os" : "Windows",
"osVersion" : "11",
"projectName" : "Sample sandbox project",
"buildName" : "Build #1",
"sessionName" : "My First Test",
},
"browserName" : "Chrome",
"browserVersion" : "latest",
}


driver = webdriver.Chrome("/Users/ssinc/Downloads/chromedriver_mac_arm64/chromedriver")


#Prompt the user for a password without echo


# username = input("Enter your user name: ")

# password = getpass("Enter in your password: ")

username = 'hero@swarajstudios.com'
password = 'cL@P1dd$5xqQ0A'

#Configure the Google Chrome browser

driver = webdriver.Remote(
    command_executor=BROWSERSTACK_URL,
    desired_capabilities=desired_cap
)

# Visit the Amazon login page

driver.get("https://www.amazon.in/")

SignIn_button = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')

SignIn_button.click()

username_textbox = driver.find_element_by_id("ap_email")

username_textbox.send_keys(username)

Continue_button = driver.find_element_by_id("continue")

Continue_button.submit()

password_textbox = driver.find_element_by_id("ap_password")

password_textbox.send_keys(password)

SignIn_button = driver.find_element_by_id("auth-signin-button-announce")

SignIn_button.submit()


driver.quit()
