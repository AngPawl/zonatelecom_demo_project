import allure
from selene import browser, have, be


class MainPage:
    def __init__(self):
        self.slider_buttons = browser.all('[data-testid^="slider."]')

    @allure.step('Открыть страницу по кнопке {button_name}')
    def open_page_via_banner(self, button_name):
        self.slider_buttons.element_by(have.exact_text(button_name)).with_(
            timeout=15
        ).wait_until(be.visible)
        self.slider_buttons.element_by(have.exact_text(button_name)).click()
