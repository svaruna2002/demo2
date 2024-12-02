# while i am using 4 version of selenium if my chrome gets update i dont have to worry
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# I want you guys to click on any one of the checkbox
# the below code is using css selctor with id
# driver.find_element(By.CSS_SELECTOR,'#checkBoxOption1').click()
# can i wrtie the same line using CSS selecctor using attributes(mulitple attribute)
# driver.find_element(By.CSS_SELECTOR,'[id="checkBoxOption1"][name="checkBoxOption1"]')
# in THe below code i am trying to identify with xpath
# driver.find_element(By.XPATH,"//*[@id='checkBoxOption1' and @name='checkBoxOption1']").click()
# i want to write a line which will identify all the checkbox and click on all checkboxes

# CHECK ALL THE CHECKBOXES
# TAG NAME IS COMMON TO ALL THE CHECKBOXES
# if there is no tag name - common

#VERSION 1
#allcheckboxes = driver.find_elements(By.XPATH, '//*[contains(@id,"checkBoxOption")]')

# VERSION2
#allcheckboxes = driver.find_elements(By.CSS_SELECTOR, '[type="checkbox"]')

# for i in allcheckboxes:
#      i.click()

# if i use //*[contains(@name,'Suni')] (sunil should be part of bigger text)

#CLICK ON ANY 2 CHECKBOXES
#version 1
# allcheckbox = driver.find_elements(By.XPATH,'//*[contains(@id,"checkBoxOption")]')
# for i in allcheckbox:
#     #i is not fetching me the text (i is one of the element)
#     if i.get_attribute("value") == "option1" or i.get_attribute("value") == "option3":
#             i.click()

#version 2
# allcheckbox = driver.find_elements(By.XPATH,'//*[contains(@id,"checkBoxOption")]')
# #list with the options i want to select
# values = ['option1','option2']
# for i in allcheckbox:
#     if i.get_attribute("value") in values:
#         i.click()


# DROPDOWN
# drop = Select(driver.find_element(By.CSS_SELECTOR,"#dropdown-class-example"))
#drop.select_by_visible_text('Option1')
#drop.select_by_index(2)
# drop.select_by_value("option3")

#VISIBLE TEXT VS INDEX VS VALUE - IMPORTANT

# IF THERE IS A DROP DOWN, IF I WANT TO SELCT 1ST OPTION, THEN FIRST SELECTED OPTION
# opt = drop.first_selected_option
# print(opt)

# WANT TO FECTH ALL THE DROPDOWN VALUES
# opt1 = drop.options
# print(len(opt1))  # NO OF VALUES IN DROPDOWN
# for i in opt1:
#     print(i.text)

# WANT TO SELECT MULTIPLE VALUES IN THE DROPDOWN, SELCT OPTION1 AND THEN OPTION 2
# TESTER OPTION - TO CHECK IF THE CLICKED OPTION IS GETTING REFLECTED
# for i in opt1:
#     if i.text =="Option1" or i.text == "Option2":
#         i.click()


#DYNAMIC DROPDOWN
#INSPECT MY ID
# to identify the class name - dot
# driver.find_element(By.CSS_SELECTOR,'#autocomplete').send_keys('Ind')
# time.sleep(2)
# list_country = driver.find_element(By.CSS_SELECTOR,".ui-menu-item div")
# for i in list_country:
#     if i.text == "India":
#         i.click()
#         time.sleep(2)


