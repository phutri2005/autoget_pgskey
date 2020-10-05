from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


import os
import time

# Set environment variables
#os.environ['webdriver.chrome.driver'] = 'F:\DevTools\chromedriver_win32_85\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(executable_path='F:\DevTools\chromedriver_win32_85\chromedriver_hex.exe', options=options)

def checkExistsCheckOut(browser):
    try:
         browser.find_element_by_partial_link_text('Checkout')
    except NoSuchElementException:
        return False
    return True

def clickCheckout(browser):
    #ActionChains(browser).click(browser.find_element_by_xpath('//*[@id="checkout"]')).perform()
    #browser.find_element_by_link_text('Checkout').click()
    browser.find_element_by_partial_link_text('Checkout').click()
    #firstname
    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Tri')
    #lastname
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Pham')
    #email
    email = browser.find_element_by_name('email')
    email.send_keys('@gmail.com')
    #fone
    phonenumber = browser.find_element_by_name('phonenumber')
    phonenumber.send_keys('773122123')
    #Street
    address1 = browser.find_element_by_name('address1')
    address1.send_keys('Huynh Tan Phat')
    #CT
    city = browser.find_element_by_name('city')
    city.send_keys('Ho Chi Minh')
    #State
    state = browser.find_element_by_name('state')
    state.send_keys('HCM')
    #Post Code
    postcode = browser.find_element_by_name('postcode')
    postcode.send_keys('700000')
    #Password
    password = browser.find_element_by_name('password')
    password.send_keys('')
    #Repeat pw
    password2 = browser.find_element_by_name('password2')
    password2.send_keys('')
    #Optional company
    companyname = browser.find_element_by_name('companyname')
    companyname.send_keys('TMA')
    #Focus to window
    browser.switch_to.window(browser.current_window_handle)
    browser.minimize_window()
    browser.maximize_window()

    
#MAIN LOGIN

while False == checkExistsCheckOut(browser):
    time.sleep(1)
    result = browser.get('https://manage.pgsharp.com/cart.php?a=add&pid=2')
    
clickCheckout(browser)
