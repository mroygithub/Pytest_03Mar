import sys
import pytest
sys.path.append('/Users/mithunroy/PycharmProjects/TrainingPytest')
from pageObject.Docker_Home import Docker_Home
from locatorsHTML import googlelocator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("multiple_browser")
class TestDockerApp:

    def test_docker_logo(self, jsonData):

        obj = Docker_Home(self.driver)
        obj.launch_app_with_url(jsonData['url_docker'])
        obj.print_all_docker_links()

