import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By


#иницилизирую драйвер браузера
driver = webdriver.Chrome()






try:
        # через get мы говорим браузеру что обращаемся к странице
    driver.get('https://erikdark.github.io/Qa_autotest_01/')
    time.sleep(2)
    #с помощью команды find_element(и класса By внутри ) мы ишем нужный элемент на странце сайта, в качестве аргумента мы передаем класс поиска By и значение которое ищем.
    btns = driver.find_elements(By.CSS_SELECTOR, '.btn')
    
    print(len(btns))
    if len(btns) == 8:
        print('da')
    else:
        print('no')

finally:
    driver.close()
