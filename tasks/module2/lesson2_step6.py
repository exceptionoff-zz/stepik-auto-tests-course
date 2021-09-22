from selenium import webdriver
import time
import math

def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_ = browser.find_element_by_id('input_value').text
    y_ = func(x_)

    line_edit = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", line_edit);
    line_edit.send_keys(y_)

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

