import allure

from litres_test.pages.main_page import MainPage


def test_activate_promocode():
    main_page = MainPage()

    with allure.step("Открываем браузер"):
        main_page.browser_open()

    with allure.step("Переходим на страницу промокодов"):
        main_page.redirect_to_promocodes()

    with allure.step('Заполняем поле промокода'):
        main_page.fill_promocode_input('promokodibonus2')

    with allure.step("Нажимаем кнопку Активировать"):
        main_page.click_activation_button()