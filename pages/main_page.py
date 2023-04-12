from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(MainPageLocators.how, MainPageLocators.what)
        login_link.click()

    # def should_be_login_link(self):
    #     assert self.is_element_present(MainPageLocators.how, MainPageLocators.what), "Ссылка на логин отсутствует"

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(LoginPageLocators.how, LoginPageLocators.what_url), "Ссылка на логин отсутствует"

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.how, LoginPageLocators.what_login_form), "Форма авторизации отсутствует"

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.how, LoginPageLocators.what_reg_form), "Форма регистрации отсутствует"
