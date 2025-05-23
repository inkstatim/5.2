class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://www.saucedemo.com"

    def navigate_to(self, url=""):
        self.page.goto(f"{self.base_url}{url}")

    def get_element_text(self, selector):
        return self.page.text_content(selector)

    def is_element_visible(self, selector):
        return self.page.is_visible(selector)

    def click_element(self, selector):
        self.page.click(selector)

    def fill_input(self, selector, value):
        self.page.fill(selector, value)