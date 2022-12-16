#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from playwright.sync_api import sync_playwright

# 동기화 방식
play_wright = sync_playwright().start()

#브라우저가 보이도록 headless옵션을 끄고, 엣지브라우저를 사용합니다.
browser = play_wright.chromium.launch(headless=False, channel="msedge")
context = browser.new_context()

#브라우저로 웹페이지를 실행합니다
page = context.new_page()

#아래 주소로 이동합니다.
page.goto("https://mandloh.tistory.com/manage/posts/")

#playwright를 종료합니다.
play_wright.stop()

