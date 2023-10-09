import allure
from selene import browser, have


class UisKaluzhskoePage:
    def __init__(self):
        self.title = browser.element('div h1')

    @staticmethod
    @allure.step('Переключиться на новую вкладку браузера')
    def switch_to_the_page():
        window = browser.driver.window_handles[-1]
        browser.driver.switch_to.window(window)

    @allure.step('Заголовок страницы имeет корректное наименование: {name}')
    def title_should_have_correct_name(self, name):
        self.title.should(have.exact_text(name))
