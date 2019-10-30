import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class SignupFB(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("https://www.facebook.com")
        #self.assertIn("Facebook", driver.title)

        self.firstname = driver.find_element_by_name('firstname')
        self.lastname = driver.find_element_by_name('lastname')
        self.email = driver.find_element_by_name('reg_email__')
        self.confirmemail = driver.find_element_by_name('reg_email_confirmation__')
        self.password = driver.find_element_by_name('reg_passwd__')
        self.date = driver.find_element_by_name('birthday_day')
        self.gender = driver.find_element_by_name('sex')
        self.signupbutton = driver.find_element_by_name('websubmit')
        with open('createData.json', 'r') as f:
            self.signupD = json.load(f)

        #print(self.signupD["firstName"])
    
    def test_normal_sign_up(self):
        self.firstname.send_keys(self.signupD["firstName"])

        self.lastname.send_keys(self.signupD["lastName"])
        self.email.send_keys(self.signupD["email"])
        self.confirmemail.send_keys(self.signupD["email"])
        self.password.send_keys(self.signupD["passWord"])
        self.date.click()
        self.gender.click()
        self.signupbutton.click()
        assert "signup pass" not in self.driver.page_source


    def test_small_password(self):
        self.firstname.send_keys(self.signupD["firstName"])
        self.lastname.send_keys(self.signupD["lastName"])
        self.email.send_keys(self.signupD["email"])
        self.confirmemail.send_keys(self.signupD["email"])
        self.password.send_keys(self.signupD["smallpassword"])
        self.date.click()
        self.gender.click()
        self.signupbutton.click()
        #check assertion message
        assert "Your password must be at least 6 characters long. Please try another." not in self.driver.page_source


    def test_wrong_confirmation_mail(self):
        self.firstname.send_keys(self.signupD["firstName"])
        self.lastname.send_keys(self.signupD["lastName"])
        self.email.send_keys(self.signupD["email"])
        self.confirmemail.send_keys(self.signupD["confirmemail"])
        self.password.send_keys(self.signupD["passWord"])
        self.date.click()
        self.gender.click()
        self.signupbutton.click()
        #check assertion message
        assert "Your emails do not match." in self.driver.page_source

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