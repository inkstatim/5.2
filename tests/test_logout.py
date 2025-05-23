import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_logout(browser):
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert products_page.is_products_page(), "Не удалось перейти на страницу товаров после входа"

    products_page.logout()

    assert login_page.is_login_page(), "Не удалось выйти и вернуться на страницу входа"
