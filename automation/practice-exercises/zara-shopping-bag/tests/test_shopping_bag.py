import pytest
from playwright.sync_api import sync_playwright, expect

ZARA_URL = "https://www.zara.com/il/en/"


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(ZARA_URL, wait_until="domcontentloaded")
        yield page

        context.close()
        browser.close()


def test_shopping_bag_link_is_visible(page):
    shopping_bag = page.get_by_text("Shopping Bag", exact=True)
    expect(shopping_bag).to_be_visible()


def test_shopping_bag_counter_is_zero(page):
    bag_count = page.locator("[data-qa-id='layout-header-go-to-cart-items-count']")
    expect(bag_count).to_have_text("0")
