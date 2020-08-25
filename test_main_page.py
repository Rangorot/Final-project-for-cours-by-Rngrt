from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    # ссылка с ошибкой http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    #page.go_to_login_page()
    page.should_be_login_link()
