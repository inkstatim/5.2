from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products_title = ".title"
        self.inventory_item = ".inventory_item"
        self.add_to_cart_button = "//button[text()='Add to cart']"
        self.cart_badge = ".shopping_cart_badge"
        self.cart_link = ".shopping_cart_link"
        self.burger_menu = "#react-burger-menu-btn"
        self.logout_link = "#logout_sidebar_link"

    def is_products_page(self):
        return self.is_element_visible(self.products_title) and self.get_element_text(self.products_title) == "Products"

    def add_product_to_cart(self, index=0):
        self.page.locator(self.add_to_cart_button).nth(index).click()

    def get_cart_count(self):
        if self.is_element_visible(self.cart_badge):
            return int(self.get_element_text(self.cart_badge))
        return 0

    def go_to_cart(self):
        self.click_element(self.cart_link)

    def open_burger_menu(self):
        self.click_element(self.burger_menu)

    def logout(self):
        self.open_burger_menu()
        self.page.wait_for_selector(self.logout_link, state="visible")
        self.click_element(self.logout_link)