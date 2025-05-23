from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = ".error-message-container"

    def open(self):
        self.navigate_to("/")

    def login(self, username, password):
        self.fill_input(self.username_input, username)
        self.fill_input(self.password_input, password)
        self.click_element(self.login_button)

    def get_error_message(self):
        return self.get_element_text(self.error_message)

    def is_login_page(self):
        return self.is_element_visible(self.login_button)