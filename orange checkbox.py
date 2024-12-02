from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

driver.find_element(By.LINK_TEXT, "PIM").click()
time.sleep(5)

checkbox = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
time.sleep(5)
#peter
#b = driver.find_element(By.XPATH,
#                       "(//*[@class='oxd-table-card'])[3]/div/div[2]/preceding-sibling::div/div/div/label/input")

#kannan
b= driver.find_element(By.XPATH,"(//*[@class='oxd-table-card'])[3]/div/div[2]/preceding-sibling::div/div/div/label/input")

b.send_keys(Keys.SPACE)
time.sleep(5)