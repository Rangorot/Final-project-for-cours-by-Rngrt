from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def is_message_about_empty_basket(self):
        assert 'is empty' in self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET_LINK).text, \
            'There is not a message about empty basket on the page'

    def should_not_any_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET_LINK), \
            'Any items is in the basket, but they shouldn`t be there'
