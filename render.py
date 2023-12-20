import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.set_window_size(616, 938)
driver.get('http://localhost:5000/')

# headless chromium is still mem-hungry
# the selenium driver will run in a loop
while True:
    driver.save_screenshot('tmp/source.png')
    time.sleep(17)