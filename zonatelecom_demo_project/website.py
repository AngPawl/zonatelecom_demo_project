import allure
from selene import browser

from zonatelecom_demo_project.components.header import Header
from zonatelecom_demo_project.pages.auth_page import AuthPage
from zonatelecom_demo_project.pages.main_page import MainPage
from zonatelecom_demo_project.pages.mobile_app_page import MobileAppPage
from zonatelecom_demo_project.pages.money_order_page import MoneyOrderPage
from zonatelecom_demo_project.pages.payments_letter_page import PaymentsLetterPage
from zonatelecom_demo_project.pages.uis_kaluzhskoe_page import UisKaluzhskoePage


class WebsiteManager:
    def __init__(self):
        self.main_page = MainPage()
        self.header = Header()
        self.auth_page = AuthPage()
        self.mobile_app_page = MobileAppPage()
        self.money_order_page = MoneyOrderPage()
        self.payments_letter_page = PaymentsLetterPage()
        self.uis_kaluzhskoe = UisKaluzhskoePage()

    @staticmethod
    @allure.step('Открыть вебсайт')
    def open():
        browser.open('/')


website = WebsiteManager()
