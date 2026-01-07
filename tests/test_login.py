import os
from pages.login_page import LoginPage

def test_valid_login(browser):
    page = LoginPage(browser)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")

    message_element = page.wait_for_message()

    # Scroll message into view
    browser.execute_script("arguments[0].scrollIntoView(true);", message_element)

    os.makedirs("screenshots", exist_ok=True)
    browser.save_screenshot("screenshots/valid_login.png")

    assert "You logged into a secure area!" in page.get_message_text()


def test_invalid_login(browser):
    page = LoginPage(browser)
    page.open()
    page.login("wrong", "wrong")

    message_element = page.wait_for_message()

    browser.execute_script("arguments[0].scrollIntoView(true);", message_element)

    os.makedirs("screenshots", exist_ok=True)
    browser.save_screenshot("screenshots/invalid_login.png")

    assert "Your username is invalid!" in page.get_message_text()
