import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions

def screenshot():
    # init driver
    my_options = ChromeOptions()
    my_options.add_argument("--headless=new")
    my_options.add_argument('--no-sandbox')

    driver = webdriver.Remote("http://192.168.0.40:7811", options=my_options)
    driver.set_window_size(616, 938)

    driver.get('http://192.168.0.40:7810/')
    time.sleep(1)
    driver.save_screenshot('tmp/source.png')

    driver.close()
    driver.quit()