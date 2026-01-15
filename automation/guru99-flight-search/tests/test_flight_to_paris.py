from playwright.sync_api import sync_playwright


def test_flight_to_paris():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.guru99.com/test/newtours/reservation.php")

        des = page.locator("select[name='toPort']")
        des.select_option(label="Paris")


        page.click("input[name='findFlights']")

        assert "After flight finder" in page.content()

        browser.close()
