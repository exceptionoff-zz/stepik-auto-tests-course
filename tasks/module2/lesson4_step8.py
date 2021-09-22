from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))



    browser.find_element_by_css_selector('#book').click()

    x_ = browser.find_element_by_css_selector('#input_value').text
    y_ = func(x_)
    browser.find_element_by_css_selector('#answer').send_keys(y_)
    browser.find_element_by_css_selector('#solve').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    