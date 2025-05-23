import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_complete_order_flow(browser):
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    cart_page = CartPage(browser)
    checkout_info_page = CheckoutInfoPage(browser)
    checkout_overview_page = CheckoutOverviewPage(browser)
    checkout_complete_page = CheckoutCompletePage(browser)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert products_page.is_products_page(), "Не удалось перейти на страницу товаров после входа"

    products_page.add_product_to_cart(0)
    assert products_page.get_cart_count() == 1, "Товар не был добавлен в корзину"

    products_page.go_to_cart()
    assert cart_page.is_cart_page(), "Не удалось перейти на страницу корзины"
    assert cart_page.get_cart_items_count() == 1, "Корзина не содержит ожидаемое количество товаров"

    cart_page.proceed_to_checkout()
    assert checkout_info_page.is_checkout_info_page(), "Не удалось перейти на страницу информации о заказе"

    checkout_info_page.fill_checkout_info("Tymur", "Akmd", "12345")
    checkout_info_page.continue_checkout()
    assert checkout_overview_page.is_checkout_overview_page(), "Не удалось перейти на страницу обзора заказа"

    checkout_overview_page.finish_checkout()
    assert checkout_complete_page.is_checkout_complete_page(), "Не удалось перейти на страницу завершения заказа"

    assert checkout_complete_page.get_complete_header() == "Thank you for your order!", "Неверный заголовок"
    assert checkout_complete_page.is_pony_express_visible(), "Изображение Pony Express не отображается"

    checkout_complete_page.back_to_home()
    assert products_page.is_products_page(), "Не удалось вернуться на страницу товаров"
