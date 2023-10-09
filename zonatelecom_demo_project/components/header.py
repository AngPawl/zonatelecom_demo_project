import allure
from selene import browser, have, be


class Header:
    def __init__(self):
        self.titles = browser.all('li[data-testid^="navigation.header"]')
        self.logo = browser.all('a[aria-label="Zonatelecom"] svg')
        self.phone_number = browser.element('[data-testid*=".header"] a[href^="tel:"]')
        self.auth_button = browser.element(
            '[data-testid="authorization.button.guestUser"]'
        )

    @allure.step('Заголовки имеют корректные наименования: {names}')
    def titles_should_have_correct_names(self, names):
        self.titles.should(have.exact_texts(names))

    @allure.step('Логотип отображается')
    def logo_should_be_visible(self):
        for el in self.logo:
            el.should(be.visible)

    @allure.step('Номер телефона отображается')
    def phone_number_should_be_visible(self):
        self.phone_number.should(be.visible)

    @allure.step('Открыть страницу авторизации')
    def open_auth_page(self):
        self.auth_button.with_(timeout=5).wait_until(be.clickable)
        self.auth_button.click()
