from selenium import webdriver
import time
import math

def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('.btn').click()

    browser.switch_to.window(browser.window_handles[1])

    x_ = browser.find_element_by_css_selector('#input_value').text
    y_ = func(x_)
    browser.find_element_by_css_selector('#answer').send_keys(y_)

    browser.find_element_by_css_selector('.btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    