from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, '#register_form')
    EMAIL_LINK = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_LINK = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD_LINK = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTER_LINK = (By.CSS_SELECTOR, '.col-sm-6.register_form .btn.btn-lg.btn-primary')


class ProductPageLocators:
    ADD_BUTTON_LINK = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary')
    NAME_OF_ADDED_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    AMOUNT_OF_MONEY_ADDED_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    NAME_OF_ADDED_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages  .alert.alert-safe:nth-child(1) strong')
    AMOUNT_OF_MONEY_IN_BASKET = (By.CSS_SELECTOR, '#messages  .alert.alert-safe:nth-child(3) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET_LINK = (By.CSS_SELECTOR, '#content_inner p')
    ITEM_IN_BASKET_LINK = (By.CSS_SELECTOR, '.basket-items')
