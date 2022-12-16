#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import nest_asyncio
nest_asyncio.apply()

from playwright.sync_api import sync_playwright

# %%

from playwright.sync_api import sync_playwright
pw = sync_playwright().start()

# %%
chrome = pw.chromium.launch(headless=False)
page = chrome.new_page()
page.goto("https://twitch.tv")