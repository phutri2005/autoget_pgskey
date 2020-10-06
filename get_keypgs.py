from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import os
import time

# Set environment variables
#os.environ['webdriver.chrome.driver'] = 'F:\DevTools\chromedriver_win32_85\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
delay = 10 #seconds
DRIVER_LOCATION = './chromedriver_hex.exe'
OPERA_DRIVER_LOCATION = './operadriver.exe'
PGS_URL = 'https://manage.pgsharp.com/cart.php?a=add&pid=2'
email_String = '@gmail.com'
password_String = ''


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

    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'firstname')))
        print("Checkout page is ready!")
    except TimeoutException:
        print("Load checkout page took too long")
    #firstname
    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Tri')
    #lastname
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Pham')
    #email
    email = browser.find_element_by_name('email')
    email.send_keys(email_String)
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
    password.send_keys(password_String)
    #Repeat pw
    password2 = browser.find_element_by_name('password2')
    password2.send_keys(password_String)
    #Optional company
    companyname = browser.find_element_by_name('companyname')
    companyname.send_keys('TMA')
    #Focus to window
    browser.switch_to.window(browser.current_window_handle)
    browser.minimize_window()
    browser.maximize_window()

def getWebDriver(driverLocation):
    if OPERA_DRIVER_LOCATION == driverLocation:
        print('Create Opera web driver')       
        return webdriver.Opera(executable_path=driverLocation, options=options)
    else:
        print('Create Chrome web driver')   
        return webdriver.Chrome(executable_path=DRIVER_LOCATION, options=options)

def getKey():
    try:
        browser = getWebDriver(OPERA_DRIVER_LOCATION)
        while False == checkExistsCheckOut(browser):
            time.sleep(1)
            result = browser.get(PGS_URL)
        clickCheckout(browser)
    except Exception as inst:
        print('Error. Retrying!!!')
        print(inst)
        getKey()


#Go go go
getKey()



