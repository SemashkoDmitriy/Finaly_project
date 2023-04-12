from selenium.webdriver.common.by import By

class MainPageLocators():
    how = By.CSS_SELECTOR
    what = "#login_link"
    
class LoginPageLocators():
    how = By.CSS_SELECTOR
    what_url = "#login_link"
    what_login_form = "#register_form"
    what_reg_form = "#login_form"