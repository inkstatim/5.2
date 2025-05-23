from pages.base_page import BasePage

class CheckoutInfoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_title = ".title"
        self.first_name_input = "#first-name"
        self.last_name_input = "#last-name"
        self.postal_code_input = "#postal-code"
        self.continue_button = "#continue"
        self.cancel_button = "#cancel"
        self.error_message = ".error-message-container"

    def is_checkout_info_page(self):
        return self.is_element_visible(self.checkout_title) and self.get_element_text(self.checkout_title) == "Checkout: Your Information"

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.fill_input(self.first_name_input, first_name)
        self.fill_input(self.last_name_input, last_name)
        self.fill_input(self.postal_code_input, postal_code)

    def continue_checkout(self):
        self.click_element(self.continue_button)

    def cancel_checkout(self):
        self.click_element(self.cancel_button)

    def get_error_message(self):
        return self.get_element_text(self.error_message)