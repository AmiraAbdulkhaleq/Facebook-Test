# Facebook-automation-testing

This task is to cover the registration and login automation test cases for Facebook using selenium

## Installation

Use this command

```bash
pip install selenium
```

then follow this description https://selenium-python.readthedocs.io/installation.html<br/>
Make sure that you have python3 installed

## Usage

Open your text editor and include the files in it (fbAutomation.py, createData.json AND loginData.json)
Open terminal and write this command

```python
python fbAutomation.py
```

and check the results.

### Code Snippet

```python
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
```
