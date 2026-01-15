

from playwright.sync_api import sync_playwright, expect

def test_contact_demo():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://advantageonlineshopping.com/#/")
        contact_us = page.get_by_text("CONTACT US")
        contact_us.click()

        cat= page.locator("[name='categoryListboxContactUs']")
        cat.select_option(label="Laptops")

        prod = page.locator("[name='productListboxContactUs']")
        prod.select_option(label="HP Pavilion 15z Laptop")

        mail = page.locator('[name="emailContactUs"]')
        mail.fill("test@example.com")

        sub = page.locator("[name='subjectTextareaContactUs']")
        sub.fill("Hello, I would like to return a product")

        send = page.locator("[id='send_btn']")
        send.click()

        success = page.locator(".successMessage")
        expect(success).to_be_visible(timeout=15000)
