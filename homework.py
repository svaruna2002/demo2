from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# b = driver.find_elements(By.XPATH, "(//table[@id='product'])[2]//tbody/tr/td")
# for i in b:
#     if i.text.__contains__("Postman"):
#         beforevalue = i.find_element(By.XPATH,"./preceding-sibling::td")
#         afterevalue = i.find_element(By.XPATH, "./following-sibling::td")
# print(beforevalue.text)
# print(afterevalue.text)

# for delhi
b = driver.find_elements(By.XPATH, "(//table[@id='product'])[2]//tbody/tr/td")
for i in b:
    if i.text.__contains__("Delhi"):
        beforevalue = i.find_element(By.XPATH,"./preceding-sibling::td")
        afterevalue = i.find_element(By.XPATH, "./following-sibling::td")
print(beforevalue.text)
print(afterevalue.text)

