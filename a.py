from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://quotes.toscrape.com/")
    page.get_by_role("link", name="Next").click()
    page.get_by_role("link", name="Next").click()
    page.get_by_role("link", name="Next").click()
    page.get_by_role("link", name="Next").click()
    page.get_by_role("link", name="Next").click()
    page.get_by_role("link", name="Next").click()
    page.get_by_role("link", name="Next").click()
    page.get_by_role("link", name="Next").click()
    page.get_by_role("link", name="Next").click()
    page.get_by_role("list").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
