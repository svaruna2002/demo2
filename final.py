import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

#browser commands
#driver.fullscreen_window()
#driver.refresh()

#maximize screen
driver.maximize_window()

#field inputs
# driver.find_element(By.ID,"RESULT_TextField-1").send_keys("sv")
# driver.find_element(By.ID,"RESULT_TextField-2").send_keys("rb")
# time.sleep(5)
# driver.find_element(By.ID,"RESULT_TextField-3").send_keys("9173957594")
# driver.find_element(By.ID,"RESULT_TextField-4").send_keys("India")
# time.sleep(5)
# driver.find_element(By.ID,"RESULT_TextField-5").send_keys("Chennai")
# driver.find_element(By.ID,"RESULT_TextField-6").send_keys("xyz@gmail.com")
# time.sleep(5)

#Radio
# driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()
# time.sleep(2)

#Scroll
driver.execute_script("window.scrollBy(0, 300);")


#checkbox version 1
#checkbox2 = driver.find_element(By.XPATH,"//label[normalize-space()='Sunday']').click()

time.sleep((2))
#checkbox version 2
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

#2.1 - 2 or 3 checkboxes
# val = ["CheckBox-0", "CheckBox-2"]
# for i in checkboxes:
#     if i.get_attribute("value") in val:
#         i.send_keys(Keys.SPACE)
#     time.sleep(2)

#2.2 all checkboxes
# for i in checkboxes:
#     i.send_keys(Keys.SPACE)
#     time.sleep(2)

#2.3 to get the values of the checkboxes
# for i in checkboxes:
#     val1 = i.get_attribute("id")
#     print(val1)

#dropdown
#3.1 by visible text
drop = Select(driver.find_element(By.XPATH,"//select[@id='RESULT_RadioButton-9']"))
#drop.select_by_visible_text('Morning')
# driver.refresh()
# driver.close()

#3.2 by index
#drop.select_by_index(2)

#3.3 by selecting value directly
drop.select_by_value("Radio-2")

#3.4 First selected
# opt = drop.first_selected_option
# print(opt)

#3.5 Fetch all the drop down
# opt1 = drop.options
# print(len(opt1))  # No of values
# for i in opt1:
#     print(i.text)

