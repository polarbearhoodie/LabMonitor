import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.set_window_size(616, 938)

# attempt to load the webpage
loaded = False
while not loaded:
    try:
        driver.get('http://192.168.0.40:7810/')
        loaded = True
    except selenium.common.exceptions.WebDriverException:
        loaded = False
        print("Unloaded")
        time.sleep(2)

# headless chromium is still mem-hungry
# the selenium driver will run in a loop
while True:
    driver.save_screenshot('tmp/source.png')
    time.sleep(17)