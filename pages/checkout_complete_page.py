from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_title = ".title"
        self.complete_header = ".complete-header"
        self.complete_text = ".complete-text"
        self.back_home_button = "#back-to-products"
        self.pony_express_img = "img.pony_express"

    def is_checkout_complete_page(self):
        return self.is_element_visible(self.checkout_title) and self.get_element_text(self.checkout_title) == "Checkout: Complete!"

    def get_complete_header(self):
        return self.get_element_text(self.complete_header)

    def get_complete_text(self):
        return self.get_element_text(self.complete_text)

    def is_pony_express_visible(self):
        return self.is_element_visible(self.pony_express_img)

    def back_to_home(self):
        self.click_element(self.back_home_button)