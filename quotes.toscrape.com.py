#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://quotes.toscrape.com/")

    # page.wait_for_timeout(5000)
    page.wait_for_selector('h1 > a') # wait for title

    data = []
    while True:
      all = page.query_selector_all('.quote')
      for q in all:
          info = {}
          text = q.query_selector('.text').inner_text()
          author = q.query_selector('.author').inner_text()
          info['text'] = text
          info['author'] = author
          data.append(info)

      # page.wait_for_timeout(1000)
      page.wait_for_selector('nav>ul>li>a') # prev && next
      next = page.get_by_role("link", name="Next")
      if next.count() == 0:
        print('Reach at End Page')
        break

      next.click()

    print(data)
    page.wait_for_timeout(10000)

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
