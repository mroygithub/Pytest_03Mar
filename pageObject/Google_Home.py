from selenium.webdriver.common.by import By


class Google_Home:

    def __init__(self, driver):
        self.driver = driver


    def launch_app_with_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)


    def google_logo_validation(self, logo):
        # Click Text box tab
        print(self.driver.title)
        logo = self.driver.find_elements(By.XPATH, logo)
        assert len(logo) > 0

    def google_search_type(self, searchbox , text):
        self.driver.find_element(By.XPATH, searchbox).send_keys(text)

    def validate_google_title(self, title):
        assert self.driver.title == title



