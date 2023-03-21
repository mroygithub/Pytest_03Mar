import pytest
import sys
sys.path.append('/Users/mithunroy/PycharmProjects/TrainingPytest')
from locatorsHTML import dockerLocator
from selenium.webdriver.common.by import By


class Docker_Home:

    def __init__(self, driver):
        self.driver = driver


    def launch_app_with_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)


    def print_all_docker_links(self):
        # Click Text box tab
        print(self.driver.title)
        allLinks = self.driver.find_elements(By.XPATH, dockerLocator.all_links())
        print(len(allLinks))
        for i in allLinks:
            print(i.text)




