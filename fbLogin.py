import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class LoginFB(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        
        driver.get("https://www.facebook.com")
        
        #self.assertIn("Facebook", driver.title)
        self.name = driver.find_element_by_id('email')
        self.userpassword = driver.find_element_by_id('pass')
        self.loginbutton = driver.find_element_by_id('loginbutton')
        with open('loginData.json', 'r') as f:
            self.loginD = json.load(f)
        #print(dataa['validName'])


    def test_login_in_facebook(self):

        self.name.send_keys(self.loginD["validName"])
        self.userpassword.send_keys(self.loginD["validPassword"])
        self.loginbutton.click()
        assert "Normal Login Pass" not in self.driver.page_source

    def test_login_blank_pass(self):
        self.name.send_keys(self.loginD["blnakN"])
        self.userpassword.send_keys(self.loginD["balnkPassword"])
        self.loginbutton.click()
        assert "The password that you've entered is incorrect." in self.driver.page_source
        
    def test_login_blank_email(self):
        self.name.send_keys(self.loginD["blankName"])
        self.userpassword.send_keys(self.loginD["blankP"])
        self.loginbutton.click()

        assert "The email address or phone number that you've entered doesn't match any account." in self.driver.page_source

    def test_login_both_blank(self):
        self.name.send_keys(self.loginD["bblankname"])
        self.userpassword.send_keys(self.loginD["bblankpassword"])
        self.loginbutton.click()
        assert "The email address or phone number that you've entered doesn't match any account." in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()