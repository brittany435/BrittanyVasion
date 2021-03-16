from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

usermenu = (By.PARTIAL_LINK_TEXT, "brittanye")
user = (By.ID, "relogin-user")
passw = (By.ID, "relogin_password")
submit = (By.ID, "admin-login-btn")
username = "brittanye"
password = "HireMe123!"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def login_pass(self, driver):
        driver.find_element_by_partial_link_text("brittanye")
    def valid_user_valid_pass(self, driver):
        driver.user.send_keys(username)
        driver.passw.send_keys(password)
        driver.submit.click()
        time.sleep(2)
    def valid_user_invalid_pass(self, driver):
        driver.find_element_by_id("relogin_user").send_keys(username)
        driver.find_element_by_id("relogin_password").send_keys("password")
        driver.find_element_by_id("admin-login-btn").click()
        time.sleep(2)
    def whitespace_username_left(self, driver):
        driver.find_element_by_id("relogin_user").send_keys(" " + username)
        driver.find_element_by_id("relogin_password").send_keys(password)
        driver.find_element_by_id("admin-login-btn").click()
        time.sleep(2)
    def whitespace_username_right(self, driver):
        driver.find_element_by_id("relogin_user").send_keys(username + " ")
        driver.find_element_by_id("relogin_password").send_keys(password)
        driver.find_element_by_id("admin-login-btn").click()
        time.sleep(2)
    def whitespace_password_left(self, driver):
        driver.find_element_by_id("relogin_user").send_keys(username)
        driver.find_element_by_id("relogin_password").send_keys(" " + password)
        driver.find_element_by_id("admin-login-btn").click()
        time.sleep(2)
    def whitespace_password_right(self, driver):
        driver.find_element_by_id("relogin_user").send_keys(username)
        driver.find_element_by_id("relogin_password").send_keys(password + " ")
        driver.find_element_by_id("admin-login-btn").click()
        time.sleep(2)
    def brute_force(self, driver):
        for i in range (8):
            driver.find_element_by_id("relogin_user").send_keys(username)
            driver.find_element_by_id("relogin_password").send_keys("password", Keys.RETURN)
            driver.find_element_by_id("admin-login-btn").click()
            driver.find_element_by_id("relogin_user").clear()
            driver.find_element_by_id("relogin_password").clear()
            time.sleep(1)
    def return_submit(self, driver):
        driver.find_element_by_id("relogin_user").send_keys(username)
        driver.find_element_by_id("relogin_password").send_keys(password)
        driver.find_element_by_id("relogin_password").send_keys(Keys.RETURN)
        driver.find_element_by_id("admin-login-btn").click()
        time.sleep(2)
    def lost_password(self, driver):
        try:
            driver.find_element_by_partial_link_text("Lost Password").click()
            print("Link successful.")
        except:
            print("Link failed.")
        time.sleep(1)
    