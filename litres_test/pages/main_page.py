from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def open_page(self, value):
        self.driver.get(value)

    def search_book(self, value):
        self.driver.find_element(By.CLASS_NAME, "SearchForm-module__hMZOXa__input").send_keys(value, Keys.ENTER)

    def choice_book(self, value):
        self.driver.find_element(By.LINK_TEXT, value).click()

    def add_to_basket(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='book__addToCartButton']").click()

    def open_basket(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-testid='book__goToCartButton']").click()

