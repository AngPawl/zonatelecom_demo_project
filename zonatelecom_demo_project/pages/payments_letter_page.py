import allure
from selene import browser, have


class PaymentsLetterPage:
    def __init__(self):
        self.title = browser.element('div h1')

    @allure.step('Заголовок страницы имeет корректное наименование: {name}')
    def title_should_have_correct_name(self, name):
        self.title.should(have.exact_text(name))
