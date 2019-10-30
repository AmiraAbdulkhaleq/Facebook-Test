# Facebook-automation-testing

TODO: this task is to cover the registration and login automation test cases for Facebook using selenium

## Installation

TODO: 
1- First you should install selenium python using https://selenium-python.readthedocs.io/installation.html
2- Make sure that you have python3 installed

## Usage

TODO:
1- Open your text editor and include the files in it (fbAutomation.py, createData.json AND loginData.json)
2- Open terminal and write the command : python fbAutomation.py and check the results

### Code Snippet

        def test_login_blank_pass(self):
        self.name.send_keys(self.loginD["blnakN"])
        self.userpassword.send_keys(self.loginD["balnkPassword"])
        self.loginbutton.click()
        assert "The password that you've entered is incorrect." in self.driver.page_source
