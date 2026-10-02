from playwright.sync_api import sync_playwright
from datetime import datetime
import os

folder = os.path.dirname(os.path.abspath(__file__))
filename = datetime.now().strftime("Cricbuzz_%d-%m-%Y_%H-%M-%S.png")
filepath = os.path.join(folder, filename)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(viewport={"width": 1366, "height": 900})

    # 1. Open recent matches page
    page.goto("https://www.cricbuzz.com/")
    page.wait_for_load_state("domcontentloaded")

    # 2. Click first match using XPath
    page.locator("xpath=/html/body/div[1]/main/div[1]/div[1]/div/div[1]/div/div/div/a").click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(3000)

    # 3. Screenshot
    page.screenshot(path=filepath)
    browser.close()

print("Saved:", filepath)