import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

time.sleep(5)
usernam = driver.find_element(By.NAME, "username").send_keys("Admin")
passw = driver.find_element(By.CSS_SELECTOR, ".oxd-input.oxd-input--active").send_keys("admin123")
submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "PIM").click()
time.sleep(5)
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
search_box.send_keys("Peter")
time.sleep(2)

list_values = driver.find_elements(By.CSS_SELECTOR, ".oxd-autocomplete-dropdown .oxd-autocomplete-option")
for value in list_values:
    if value.text == "Peter Mac Anderson":
        value.click()
        break
        time.sleep(2)

driver.find_element(By.XPATH,"(//*[@class ='oxd-select-text--after'])[1]").click()
values = driver.find_elements(By.CSS_SELECTOR, ".oxd-autocomplete-dropdown .oxd-autocomplete-option")
for i in values:
    if i.text == "Freelance":
        i.click()
        break
        time.sleep(2)
