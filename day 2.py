import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# To launch the browser
driver = webdriver.Firefox()

# To get the URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# To check any one of the checkboxes

# CSS selector using ID
# driver.find_element(By.CSS_SELECTOR, '#checkBoxOption1').click()

# CSS selector using attributes (multiple attributes)
# driver.find_element(By.CSS_SELECTOR, '[id="checkBoxOption1"][name="checkBoxOption1"]').click()

# Checkbox by using XPath
# driver.find_element(By.XPATH, '//*[@id="checkBoxOption1" and @name="checkBoxOption1"]').click()

checkbox = driver.find_elements(By.XPATH, '//*[@type="checkbox"]')
time.sleep(4)

# Loop through all checkboxes and select them using SPACE key
for checkboxes in checkbox:
    checkboxes.send_keys(Keys.SPACE)

time.sleep(5)
