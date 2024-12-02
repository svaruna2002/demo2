import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

# Enter username
driver.find_element(By.NAME, "username").send_keys("Admin")

# Fetch the username that was entered
user_name = driver.find_element(By.NAME, "username").get_attribute("value")
print(user_name)

# Enter password
driver.find_element(By.NAME, "password").send_keys("admin123")

# Click login button
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
time.sleep(5)

# Navigate to PIM
driver.find_element(By.LINK_TEXT, "PIM").click()
time.sleep(3)

# Fetch and print the text of the header
data1 = driver.find_element(By.TAG_NAME, "h6").text
time.sleep(5)
print(data1)

# Fetch and print the text of the link
data2 = driver.find_element(By.LINK_TEXT, "PIM").text
time.sleep(5)
print(data2)

# Assert that both texts are equal
assert data1 == data2

# Find all links on the page
All_links = driver.find_elements(By.TAG_NAME, "a")
print(len(All_links))

# Print all link texts
Links = []
for i in All_links:
    print(i.text)

time.sleep(5)

# Log out
driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").click()
driver.find_element(By.LINK_TEXT, "Logout").click()
