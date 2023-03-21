# Python code to demonstrate working of unittest
# Appium With Python
# Android Native App with Appium Python
import unittest
from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy


class TestMobileAPK:

    desired_caps = {
        "deviceName": "Samsung",
        "platformName": "Android",
        "version": "9.0",
        "udid": "11f2b948",
        "app": "/Users/mithunroy/Downloads/naukri-com-17-1.apk"
    }

    # Android Native App in Real Device using Chrome

    def launch_the_APK(self):
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        driver.update_settings({"waitForIdleTimeout": 500})

        # Validate Later/Settings Cancel button ...
    def skip_settings(self):
        try:
            time.sleep(5)
            driver.find_element(AppiumBy.ID,
                                                "naukriApp.appModules.login:id/ssa_cancel_textview").is_displayed()
            driver.find_element(AppiumBy.ID,
                                    "naukriApp.appModules.login:id/ssa_cancel_textview").click()
            time.sleep(5)
            print('Later button closed successfully')

        except:
            print('Setting option skipped ...')
    
    def test_003_Top_Companies_Flow(self):
        try:

            self.skip_settings()
            time.sleep(5)
            driver.press_keycode(4)
            time.sleep(2)

            size = driver.get_window_size()
            start_y = size['height'] * 0.9
            end_y = size['height'] * 0.1
            start_x = size['width'] * 0.5
            end_x = size['width'] * 0.2
            print(start_y)
            print(end_y)
            print(start_x)
            print(end_x)

            # python
            #driver.swipe(start_x=75, start_y=500, end_x=75, end_y=0, duration=800)
            #swipe from the bottom of the screen to the top of the screen
            #driver.swipe(470, 800, 470, 50, 400) ..... This is hardcoded and Working fine ..
            driver.swipe(start_x, start_y, end_x, end_y, 400)
            time.sleep(5)

            # Do Click on View All
            
            view_Al = driver.find_element(AppiumBy.XPATH,
                                                "//android.widget.TextView[@text='View all']")
            view_Al.click()
            time.sleep(5)


            # Count total number of compmapies present in the Screen ...

            total_comp = driver.find_elements(AppiumBy.XPATH,                    
                            "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/tv_company_name']")

            print(len(total_comp))

            for i in total_comp:
                compName = i.get_attribute('text')
                print("The Company Name is ===>"+compName)

            print('Top Companies Functionalities ..... PASS')

        except:
            print('Top Companies Functionalities  FAIL')




    # Quiting the App
    def tearDown(self):
        driver.quit()

obj  = TestMobileAPK()
obj.launch_the_APK()
obj.skip_settings()
obj.test_003_Top_Companies_Flow()
obj.tearDown()