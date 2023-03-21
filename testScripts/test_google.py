import sys
import pytest
sys.path.append('/Users/mithunroy/PycharmProjects/TrainingPytest')
from pageObject.Google_Home import Google_Home
from locatorsHTML import googlelocator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class TestGoogleApp:

    @pytest.mark.smoke
    def test_google_logo(self, browser):

        obj = Google_Home(browser)
        obj.launch_app_with_url("https://www.google.com")
        obj.google_logo_validation(googlelocator.google_logo())

    @pytest.mark.regression
    def test_google_searchbox(self, browser):

        obj = Google_Home(browser)
        obj.launch_app_with_url("https://www.google.com")

        time.sleep(3)

    @pytest.mark.smoke
    def test_google_title(self, browser):
        obj = Google_Home(browser)
        obj.launch_app_with_url("https://www.google.com")
        obj.validate_google_title("Google")