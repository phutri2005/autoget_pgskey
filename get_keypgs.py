from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

import os
import time

# Set environment variables
#os.environ['webdriver.chrome.driver'] = 'F:\DevTools\chromedriver_win32_85\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


browser = webdriver.Chrome(executable_path='./chromedriver_hex.exe', options=options)

while True:
    time.sleep(1)
    result = browser.get('https://manage.pgsharp.com/cart.php?a=add&pid=2')
    try:
        if "429" in browser.title:
            browser.refresh
        #elif "Shopping Cart" in browser.title:
        #    element = browser.find_element_by_xpath('//*[@id="order-boxes"]/div/h1')
        #   print(element.text)
        #   browser.refresh
        elif "Out of Stock" in browser.find_element_by_xpath('//*[@id="order-boxes"]/div/h1').text:
        #    element = browser.find_element_by_xpath('//*[@id="order-boxes"]/div/h1')
        #   print(element.text)
            browser.refresh
        else:
            browser.switch_to.window(browser.current_window_handle)
            browser.minimize_window()
            browser.maximize_window()
            break
    except NoSuchElementException:
        browser.switch_to.window(browser.current_window_handle)
        browser.minimize_window()
        browser.maximize_window()
        break
