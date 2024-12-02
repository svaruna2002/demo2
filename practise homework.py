from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://cosmocode.io/automation-practice-webtable/")

# extracting an element from table 2
# a = driver.find_elements(By.XPATH, "(//table[@id='countries'])[1]//tbody/tr/td")
# for i in a:
#     if i.text.__contains__("Vienna"):
#         beforevalue = i.find_element(By.XPATH,"./preceding-sibling::td/strong")
#         afterevalue = i.find_element(By.XPATH, "./following-sibling::td")
# print(beforevalue.text)
# print(afterevalue.text)

a = driver.find_elements(By.XPATH, "(//table[@id='countries'])[1]//tbody/tr/td")
for i in a:
    if i.text.__contains__("Austria"):
        beforevalue = i.find_element(By.XPATH,"./preceding-sibling::td/input[@type='checkbox']").click()
        # print(beforevalue.text) # dont type this
time.sleep(5)
