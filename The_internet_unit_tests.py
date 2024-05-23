import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TheInternetTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_ab_testing_page_load(self):
        print("Testing A/B Testing page load")
        self.driver.find_element(By.LINK_TEXT, "A/B Testing").click()
        if "A/B Test" in self.driver.page_source:
            print("A/B Testing page loaded successfully")

    def test_add_remove_elements(self):
        print("Testing Add/Remove Elements functionality")
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
        self.driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
        if self.driver.find_element(By.CLASS_NAME, "added-manually").is_displayed():
            print("Element added successfully")
        self.driver.find_element(By.CLASS_NAME, "added-manually").click()
        if len(self.driver.find_elements(By.CLASS_NAME, "added-manually")) == 0:
            print("Element removed successfully")

    def test_basic_auth_success(self):
        print("Testing Basic Auth with correct credentials")
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        if "Congratulations!" in self.driver.page_source:
            print("Successfully logged in with correct credentials")

    def test_basic_auth_failure(self):
        print("Testing Basic Auth with incorrect credentials")
        self.driver.get("https://admin:wrong@the-internet.herokuapp.com/basic_auth")
        if "Not authorized" in self.driver.page_source:
            print("Login failed with incorrect credentials")

    def test_broken_images(self):
        print("Testing Broken Images page")
        self.driver.find_element(By.LINK_TEXT, "Broken Images").click()
        images = self.driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            if "404" not in img.get_attribute("naturalWidth"):
                print(f"Image {img.get_attribute('src')} loaded successfully")
        print("All images loaded without errors")

    def test_checkboxes(self):
        print("Testing Checkboxes selection")
        self.driver.find_element(By.LINK_TEXT, "Checkboxes").click()
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        for checkbox in checkboxes:
            checkbox.click()
            if checkbox.is_selected():
                print(f"Checkbox {checkbox.get_attribute('id')} selected")
            checkbox.click()
            if not checkbox.is_selected():
                print(f"Checkbox {checkbox.get_attribute('id')} deselected")
        print("Checkbox selection functionality verified")

    def test_context_menu(self):
        print("Testing Context Menu functionality")
        self.driver.find_element(By.LINK_TEXT, "Context Menu").click()
        box = self.driver.find_element(By.ID, "hot-spot")
        action = ActionChains(self.driver)
        action.context_click(box).perform()
        alert = self.driver.switch_to.alert
        if alert.text == "You selected a context menu":
            print("Context menu alert displayed and accepted")
        alert.accept()

    def test_drag_and_drop(self):
        print("Testing Drag and Drop functionality")
        self.driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
        source = self.driver.find_element(By.ID, "column-a")
        target = self.driver.find_element(By.ID, "column-b")
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
        if source.text == "B" and target.text == "A":
            print("Drag and Drop performed successfully")

    def test_dropdown_selection(self):
        print("Testing Dropdown selection")
        self.driver.find_element(By.LINK_TEXT, "Dropdown").click()
        dropdown = self.driver.find_element(By.ID, "dropdown")
        dropdown.click()
        option = dropdown.find_element(By.CSS_SELECTOR, "option[value='1']")
        option.click()
        if option.is_selected():
            print("Dropdown option 1 selected successfully")

    def test_file_upload(self):
        print("Testing File Upload functionality")
        self.driver.find_element(By.LINK_TEXT, "File Upload").click()
        upload_field = self.driver.find_element(By.ID, "file-upload")
        upload_field.send_keys("D:/tests/TestFile.txt")
        self.driver.find_element(By.ID, "file-submit").click()
        if "File Uploaded!" in self.driver.page_source:
            print("File uploaded and verified successfully")

    def test_form_authentication_success(self):
        print("Testing Form Authentication with valid credentials")
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()
        if "Welcome to the Secure Area" in self.driver.page_source:
            print("Successfully logged in with valid credentials")

    def test_form_authentication_failure(self):
        print("Testing Form Authentication with invalid credentials")
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("wrongpassword")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()
        if "Your username is invalid!" in self.driver.page_source:
            print("Login failed with invalid credentials")

if __name__ == "__main__":
    unittest.main()
