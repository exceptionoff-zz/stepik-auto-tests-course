from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x)
    field = browser.find_element_by_id('answer')    
    field.send_keys(y)
    check_box = browser.find_element_by_id('robotCheckbox')
    check_box.click()
    radio_btn = browser.find_element_by_id('robotsRule')
    radio_btn.click()
    btn = browser.find_element_by_css_selector('.btn')
    btn.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()