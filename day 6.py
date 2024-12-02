from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import Keys

# Initialize the WebDriver
driver = webdriver.Firefox()

# Open the target URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize the browser window
driver.maximize_window()

# Wait for 3 seconds
time.sleep(3)

# Enter username and password
#username = driver.find_element(By.NAME, "username").send_keys("Admin")
#password = driver.find_element(By.NAME, "password").send_keys("admin123")

# Wait for 2 seconds
time.sleep(2)

# Click the login button
#button = driver.find_element(By.CSS_SELECTOR, ".oxd-button ").click()

# Wait for 3 seconds
time.sleep(3)

#this will open a new tab and focus will remain on the same tab, new tab, focus on same tab
#driver.execute_script("window.open('https://www.google.com')")

# Click the link to navigate to the next page
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

# Wait for 3 seconds
time.sleep(3)

# for orange HRM, the focus is on old tab, because the link is in organge hrm


#current window - parent window other are child window
#no title is printed becuase we are using window handle for last commented line
first = driver.current_window_handle
driver.switch_to.window(first)
print(driver.title)
#print(first.title())


#how many tabs are opened
#driver.window handles will try to fetch both parent and child window
all = driver.window_handles
print(len(all))
secondtab= driver.switch_to.window(all[1])
print(driver.title)
driver.find_element(By.XPATH, "(//*[contains(text(), 'Book a Free Demo')])[2]").click()

driver.switch_to.window(first)
driver.find_element((By.NAME, "username").send_keys("Admin"))
driver.close()
driver.quit()


# from parent, n no of child window
# can choose any specific tab



