import allure
from allure_commons.types import Severity

from zonatelecom_demo_project.website import website


@allure.title('Страница "Мобильное приложение Зонателеком" успешно открывается')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_mobile_app_page_successfully_opens_via_banner(browser_setup):
    website.open()

    website.main_page.open_page_via_banner('Установить приложение')

    website.mobile_app_page.title_should_have_correct_name(
        'Мобильное приложение Зонателеком'
    )


@allure.title(
    'Страница "Отправить деньги заключенному в СИЗО и ИК" успешно открывается'
)
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_money_order_page_successfully_opens(browser_setup):
    website.open()

    website.main_page.open_page_via_banner('Перевести')

    website.money_order_page.title_should_have_correct_name(
        'Отправить деньги заключенному в СИЗО и ИК'
    )


@allure.title(
    'Страница "Отправка писем в СИЗО, ИК и другие исправительные учреждения" успешно открывается'
)
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_payments_letter_page_successfully_opens(browser_setup):
    website.open()

    website.main_page.open_page_via_banner('Подробнее')

    website.payments_letter_page.title_should_have_correct_name(
        'Отправка писем в СИЗО, ИК и другие исправительные учреждения'
    )


@allure.title(
    'Страница "Сервис по формированию и вручению передач АО "Предприятие УИС "Калужское" '
    'приветствует Вас" успешно открывается'
)
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_uis_kaluzhskoe_successfully_opens(browser_setup):
    website.open()

    website.main_page.open_page_via_banner('Заказать')
    website.uis_kaluzhskoe.switch_to_the_page()

    website.uis_kaluzhskoe.title_should_have_correct_name(
        'Сервис по формированию и вручению передач АО "Предприятие УИС "Калужское" приветствует Вас'
    )
