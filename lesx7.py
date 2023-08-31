from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import os
import time
link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    browser.switch_to.window(browser.window_handles[1])
finally:
    time.sleep(1) 
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    try:
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        print(x)
        y = calc(x)
        y_element = browser.find_element(By.ID,"answer")
        print(y)
        y_element.send_keys(y)
        button = browser.find_element(By.TAG_NAME, 'button')
        button.click()
    finally:
        time.sleep(20)
        browser.quit()
    
