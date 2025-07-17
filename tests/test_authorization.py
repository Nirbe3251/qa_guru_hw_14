import allure

from litres_test.pages.main_page import MainPage

def test_login():
    main_page = MainPage()

    main_page.browser_open()
    main_page.open_login_popup()
    main_page.fill_email()
    main_page.fill_password()