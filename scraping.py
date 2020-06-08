from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.forbes.com/under30/list/2019/asia/#3075a58b7572')
time.sleep(3)
click_element = driver.find_element_by_class_name("icon icon-search")

