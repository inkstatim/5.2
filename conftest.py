import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        console_errors = []

        page.on("console", lambda msg:
            console_errors.append(msg.text) if msg.type == "error" else None)

        yield page

        if console_errors:
            print(f"ошибки в консоли: {console_errors}")

        context.close()
        browser.close()