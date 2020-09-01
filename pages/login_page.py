from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert '/login/' in login_url, 'Not a login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), 'Not a form for log in'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), 'Not a form for register'

    def register_new_user(self, email, password):
        field_for_email = self.browser.find_element(*LoginPageLocators.EMAIL_LINK)
        field_for_email.send_keys(email)
        field_for_password = self.browser.find_element(*LoginPageLocators.PASSWORD_LINK)
        field_for_password.send_keys(password)
        field_for_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_LINK)
        field_for_confirm_password.send_keys(password)
        button_for_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER_LINK)
        button_for_registration.click()


