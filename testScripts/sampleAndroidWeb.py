# Python code to demonstrate working of unittest
# Appium With Python
# Android Web using Chrome with Appium Python
import unittest
from appium import webdriver


class TestMobileChrome(unittest.TestCase):
    desired_caps = {
        "deviceName": "Samsung",
        "platformName": "Android",
        "version": "9.0",
        "udid": "11f2b948",
        "browserName": "chrome"
    }

    # Launch Chrome Browser in Real Device using Chrome

    def setUp(self):
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        driver.get("https://www.google.com")

    # Validate Google Page Title
    def test_googleTitle(self):
        self.assertEqual(driver.title, 'Google')
        print('Google Title Validation is Pass')

    # Quiting the Browser
    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()