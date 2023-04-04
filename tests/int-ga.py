from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# userName = os.environ['BROWSERSTACK_USERNAME']
# accessKey = os.environ['BROWSERSTACK_ACCESS_KEY']
# localIdentifier = os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
# buildName = os.environ['BROWSERSTACK_BUILD_NAME']
# projectName = os.environ['BROWSERSTACK_PROJECT_NAME']

userName = 'sridharmachani_cVTeOt'
accessKey = 'vEKxcBixzrsra51FAR2B'
localIdentifier = '1'
buildName = 'BS test v1'
projectName = 'BS test 2'

bstack_options = {
    "os" : "Windows",
    "osVersion" : "10",
    "buildName" : "BStack Build Name: " + buildName,
    "projectName" : "BStack Project Name: " + projectName,
    "localIdentifier": localIdentifier,
    "seleniumVersion" : "4.0.0",
    "userName": username,
    "accessKey": accessKey
}
options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)
driver.get("http://localhost:8000") # HTTP Server should be running on 8000 port of GitHub runner
print(driver.title)
driver.quit()
