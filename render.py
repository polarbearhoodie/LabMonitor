import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.common import exceptions

def init_diver():
    # init driver
    my_options = ChromeOptions()
    my_options.add_argument("--headless=new")

    # docker specific
    my_options.add_argument('--no-sandbox')
    my_options.add_argument("--remote-debugging-port=9222")
    my_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Remote("http://192.168.0.40:7811", options=my_options)
    driver.set_window_size(616, 938)

    return driver

def save_image(browser_driver):
    # attempt to load the webpage
    try:
        browser_driver.get('http://192.168.0.40:7810/')
    except exceptions.WebDriverException:
        time.sleep(0.5)
        browser_driver.get('http://192.168.0.40:7810/')

    browser_driver.save_screenshot('tmp/source.png')

