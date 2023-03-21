import sys
import pytest
from pathlib import Path
#sys.path.append('/Users/mithunroy/PycharmProjects/TrainingPytest')
sys.path.append(str(Path(__file__).parent.parent))
from selenium.webdriver.common.by import By
import time
from appium import webdriver



#@pytest.mark.usefixtures("appiumdriver")
class TestDockerAppiumWeb:

    capabilities = {

        "deviceName":"Samsung Galaxy",
        "platformName":"Android",
        "platformVersion":"11.1",
        "browserName":"chrome",
        "udid":"11f2b948"
    }

    def test_docker_logo(self):
        
        driver = webdriver.Remote("https://localhost:4723/wd/hub" ,self.capabilities)
        print("Started testing in Android Real Device Web App using Appium")
        driver.get("https://www.docker.com")
        docker_logo = self.driver.find_elements(By.XPATH, "//li[@class='logo']")
        assert len(docker_logo) > 0

   