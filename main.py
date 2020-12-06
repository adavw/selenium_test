from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
target_url = ""
while not target_url:
    target_url = input("Target URL: ")
    title_assert = input("Title assertion: ")

if target_url:
    chrome_options.add_argument("--headless")
    chrome_browser = webdriver.Chrome('./chromedriver', options=chrome_options)
    chrome_browser.get(target_url)
try:
    assert title_assert in chrome_browser.title
except AssertionError:
    print(f"The string {title_assert} was not found in the Title.")
finally:
#found_element = chrome_browser.find_element_by_name("q")
    chrome_browser.close()