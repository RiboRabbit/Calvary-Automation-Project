from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()


driver.maximize_window()

driver.get('http://202.153.33.67/sponsors/index')   

sleep(1)

driver.find_element_by_id("user_name").send_keys("ongole") 
driver.find_element_by_id("password").send_keys("Ogl#Spnr")


location = Select(driver.find_element_by_id("location"))

location.select_by_value('6')

driver.find_element_by_xpath("/html/body/div[2]/div/form/div[4]/button").click()

sleep(1)

driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div/a/div[2]/h3").click()

driver.find_element_by_id("keywords").send_keys("9703129938")


driver.find_element_by_xpath("//*[@id='searchForm']/div/div[2]/a[1]").click()

sleep(1)

driver.find_element_by_xpath("//*[@id=\"sponsorBody\"]/div/table/tbody/tr/td[6]/a[1]").click()

#  
