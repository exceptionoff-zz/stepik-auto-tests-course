from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    
    sum_ = str(int(num1) + int(num2))
    
    web_list = Select(browser.find_element_by_id('dropdown'))
    web_list.select_by_value(sum_)
    
    btn = browser.find_element_by_css_selector('.btn')
    btn.click()
    
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()