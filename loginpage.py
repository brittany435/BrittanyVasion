import unittest
import page
from selenium import webdriver
import time

class LoginScreen(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://brittanye.printercloud.com/admin/")
        time.sleep(1)
    
    def test_1_validuservalidpass(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.valid_user_valid_pass(self.driver)
        assert loginPage.login_pass(self.driver)

    def test_2_validuserinvalidpass(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.valid_user_invalid_pass(self.driver)
        assert loginPage.login_pass(self.driver)    

    def test_3_whitespaceuserleft(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.whitespace_username_left(self.driver)
        assert loginPage.login_pass(self.driver) 

    def test_4_whitespaceuserright(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.whitespace_username_right(self.driver)
        assert loginPage.login_pass(self.driver)

    def test_5_whitespacepassleft(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.whitespace_password_left(self.driver)
        assert loginPage.login_pass(self.driver)

    def test_6_whitespacepassright(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.whitespace_password_right(self.driver)
        assert loginPage.login_pass(self.driver)
    
    # def test_7_bruteforce(self):
    #     loginPage = page.LoginPage(self.driver)
    #     loginPage.brute_force(self.driver)
    #     assert loginPage.login_pass(self.driver)

    def test_8_returnsubmit(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.return_submit(self.driver)
        assert loginPage.login_pass(self.driver)
    
    def test_9_lostpassword(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.lost_password(self.driver)
        assert loginPage.login_pass(self.driver)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()