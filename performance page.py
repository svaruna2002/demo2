import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.maximize_window()

#login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(5)

#navigating to Performance Page
driver.find_element(By.LINK_TEXT, "Performance").click()
time.sleep(5)

#clicking on configure
driver.find_element(By.XPATH, "//span[normalize-space()='Configure']").click()
time.sleep(3)

#hover to  configure - KPI
element_to_hover = driver.find_element(By.CLASS_NAME, "oxd-topbar-body-nav-tab-link")

actions = ActionChains(driver)
actions.move_to_element(element_to_hover).perform()
time.sleep(3)

element_to_hover.click()
time.sleep(3)

#KPI Page - selecting from a dropdown
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Finance Manager']").click()
time.sleep(5)

#search & research button
# driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
# time.sleep(5)

driver.find_element(By.XPATH, "//button[normalize-space()='Reset']").click()
time.sleep(5)

#scrolling down
driver.execute_script("window.scrollBy(0, 500);")

#adding a record
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
time.sleep(3)

#selecting KPI and job
# input_element = driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']")
# input_element.send_keys("Customer Service")
# time.sleep(5)

driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Finance Manager']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
time.sleep(5)
