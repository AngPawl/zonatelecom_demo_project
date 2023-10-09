import allure
from allure_commons.types import Severity

from zonatelecom_demo_project.website import website


@allure.title('Страница авторизации успешно открывается')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_auth_page_successfully_opens(browser_setup):
    website.open()

    website.header.open_auth_page()

    website.auth_page.auth_form_should_be_visible()
    website.auth_page.auth_form_input_should_be_visible_and_clickable()
    website.auth_page.auth_form_button_should_be_visible_and_clickable()
