import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

time.sleep(4)
usernam = driver.find_element(By.NAME, "username").send_keys("Admin")
passw = driver.find_element(By.CSS_SELECTOR, ".oxd-input.oxd-input--active").send_keys("admin123")
submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Leave").click()
time.sleep(4)

#Navigating to leave page

rightclick = driver.find_element(By.LINK_TEXT, "Leave")
time.sleep(3)
actions = ActionChains(driver)
actions.context_click(rightclick)
actions.key_down(Keys.CONTROL).click(rightclick).key_up(Keys.CONTROL).perform()
time.sleep(2)
win = driver.window_handles
driver.switch_to.window(win[1])
time.sleep(2)
# driver.close()
driver.quit()