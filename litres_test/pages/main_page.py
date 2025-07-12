from selene import browser, have, be, command


class MainPage:
    def browser_open(self):
        browser.open("https://www.litres.ru/")

    def search_book(self, value):
        browser.element("[name='q']").type(value).press_enter()

    def open_book(self):
        browser.element('[data-testid="art__title"][href="/audiobook/stiven-king/mertvaya-zona-65822193/"]').should(be.visible).click()
        browser.driver.switch_to.window(browser.driver.window_handles[-1])  # Переключаемся на вкладку с книгой

    def add_book_in_the_cart(self):
        element = browser.element("[data-testid='book__addToCartButton']").should(be.visible)
        browser.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element.locate())
        element.should(be.clickable).click()

    def redirect_to_cart(self):
        browser.element('[data-testid="modal__close--button"]').click()
        browser.element("[data-testid='book__goToCartButton']").click()


    def remove_book_from_the_cart(self):
        browser.element("[data-testid='cart__listDeleteButton']").click()
        browser.element('//*[@id="modal"]/div[3]/div/div/div/div/div[3]/button[1]').click()


