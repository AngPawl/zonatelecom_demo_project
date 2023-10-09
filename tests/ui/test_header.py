import allure
from allure_commons.types import Severity

from zonatelecom_demo_project.website import website


@allure.title('Заголовки страниц имеют корректное наименование')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_header_titles_have_correct_names(browser_setup):
    website.open()

    website.header.titles_should_have_correct_names(
        ['Сервисы', 'Оплата', 'Учреждениям', 'О компании', 'Поддержка']
    )


@allure.title('Логотип отображается на странице')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_header_logo_should_be_visible(browser_setup):
    website.open()

    website.header.logo_should_be_visible()


def test_header_phone_number_should_be_visible(browser_setup):
    website.open()

    website.header.phone_number_should_be_visible()
