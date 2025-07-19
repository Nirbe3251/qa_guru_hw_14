import allure

from litres_test.pages.main_page import MainPage



def test_login():
    main_page = MainPage()

    with allure.step("Открываем браузер"):
        main_page.browser_open()

    with allure.step("Открываем попап логина"):
        main_page.open_login_popup()

    with allure.step("Заполняем почту"):
        main_page.fill_email('daniil.efimow@mail.ru')

    with allure.step("Заполняем пароль"):
        main_page.fill_password('dandris2003')