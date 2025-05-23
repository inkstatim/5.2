from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_title = ".title"
        self.cart_item = ".cart_item"
        self.finish_button = "#finish"
        self.cancel_button = "#cancel"
        self.summary_subtotal = ".summary_subtotal_label"
        self.summary_tax = ".summary_tax_label"
        self.summary_total = ".summary_total_label"

    def is_checkout_overview_page(self):
        return self.is_element_visible(self.checkout_title) and self.get_element_text(self.checkout_title) == "Checkout: Overview"

    def get_cart_items_count(self):
        return len(self.page.locator(self.cart_item).all())

    def get_subtotal(self):
        text = self.get_element_text(self.summary_subtotal)
        return float(text.split("$")[1])

    def get_tax(self):
        text = self.get_element_text(self.summary_tax)
        return float(text.split("$")[1])

    def get_total(self):
        text = self.get_element_text(self.summary_total)
        return float(text.split("$")[1])

    def finish_checkout(self):
        self.click_element(self.finish_button)

    def cancel_checkout(self):
        self.click_element(self.cancel_button)