import allure
from selene import browser, be


class AuthPage:
    def __init__(self):
        self.auth_form = browser.element('div form')
        self.button = browser.element(
            'button[data-testid="authorization.form.submitPhoneButton"]'
        )
        self.input = browser.element('[data-testid="authorization.form.phoneInput"]')

    @allure.step('Форма авторизации отображается')
    def auth_form_should_be_visible(self):
        self.auth_form.with_(timeout=5).should(be.visible)

    @allure.step('Кнопка формы авторизации отображается и кликабельная')
    def auth_form_button_should_be_visible_and_clickable(self):
        self.button.should(be.visible)
        self.button.should(be.clickable)

    @allure.step('Поле ввода формы авторизации отображается и кликабельное')
    def auth_form_input_should_be_visible_and_clickable(self):
        self.input.should(be.visible)
        self.input.should(be.clickable)
