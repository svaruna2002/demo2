import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
gmail = driver.find_element(By.LINK_TEXT, "Gmail")
actions = ActionChains(driver)
actions.context_click(gmail).perform()
time.sleep(5)
# actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
actions.key_down(Keys.CONTROL).click(gmail).key_up(Keys.CONTROL).perform()
window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])
time.sleep(10)