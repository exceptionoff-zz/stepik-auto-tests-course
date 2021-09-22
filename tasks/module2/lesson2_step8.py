from selenium import webdriver
import time
import os




try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('[name="firstname"]').send_keys('Nikolai')
    browser.find_element_by_css_selector('[name="lastname"]').send_keys('Kuvshinov')
    browser.find_element_by_css_selector('[name="email"]').send_keys('123@mail.ru')

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'test.txt')

    browser.find_element_by_css_selector('#file').send_keys(file_path)

    browser.find_element_by_css_selector('.btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    