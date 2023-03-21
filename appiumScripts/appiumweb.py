from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class DeckerApp:

    desired_caps = {
        "deviceName": "Samsung",
        "platformName": "Android",
        "version": "9.0",
        "udid": "11f2b948",
        "browserName": "chrome"
    }


    def launch_Appium_Driver(self):

        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        driver.get("https://www.docker.com")

    def docker_logo_validation(self):

        try:
            if driver.find_element(AppiumBy.XPATH , "//li[@class='logo']").is_displayed():
                print("Docker logo is present")
        except: 
                print("Docker logo is not present")       

    def close_driver(self):
        driver.quit
    
obj = DeckerApp()
obj.launch_Appium_Driver()
obj.docker_logo_validation()
obj.close_driver()


