#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import nest_asyncio
nest_asyncio.apply()

from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://tcafe2a.com/")
    page.locator("#ol_id").click()
    page.locator("#ol_id").fill("mkeasy")
    page.locator("#ol_pw").click()
    page.locator("#ol_pw").fill("dodls9gka")
    page.get_by_role("button", name="로그인").click()
    page.locator("#thema_wrapper").get_by_role("link", name="출석확인").click()
    page.locator("#cnftjr img").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
