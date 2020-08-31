from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON_LINK)
        button_add_to_basket.click()

    def should_names_are_the_same(self):
        product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_ADDED_PRODUCT_IN_BASKET).text
        product_has_added = self.browser.find_element(*ProductPageLocators.NAME_OF_ADDED_PRODUCT).text
        assert product_in_basket == product_has_added, 'Wrong name of added product'

    def should_prices_are_the_same(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_MONEY_IN_BASKET).text
        price_of_product_has_added = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_MONEY_ADDED_PRODUCT).text
        assert price_in_basket == price_of_product_has_added, 'Wrong amount of money for added products'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
