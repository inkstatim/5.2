from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_title = ".title"
        self.cart_item = ".cart_item"
        self.checkout_button = "#checkout"
        self.continue_shopping_button = "#continue-shopping"

    def is_cart_page(self):
        return self.is_element_visible(self.cart_title) and self.get_element_text(self.cart_title) == "Your Cart"

    def get_cart_items_count(self):
        return len(self.page.locator(self.cart_item).all())

    def proceed_to_checkout(self):
        self.click_element(self.checkout_button)

    def continue_shopping(self):
        self.click_element(self.continue_shopping_button)