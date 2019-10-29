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
        self.username = driver.find_element_by_id('u_0_o')
        self.email = driver.find_element_by_id('u_0_r')
        self.confirmemail = driver.find_element_by_id('u_0_u')
        self.password = driver.find_element_by_id('u_0_y')
        self.date = driver.find_element_by_id('u_0_6')
        self.gender = driver.find_element_by_id('day')
        self.signupbutton = driver.find_element_by_id('u_0_15')
#        dataa = json.loads(data.json)

'''
    def signuppp(self):
        self.username.send_keys('Amira')
        self.email.send_keys('Amira@bla.com')
        self.confirmemail.send_keys('Amira@bla.com')
        self.password.send_keys('123987**')
        self.date.click()
        self.gender.click()
        self.signupbutton.click()
        assert "signup pass" not in self.driver.page_source

    
#    def tearDown(self):
 #       self.driver.close()
'''
if __name__ == "__main__":
    unittest.main()