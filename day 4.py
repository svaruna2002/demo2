from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Google homepage
#driver.get("https://google.com/")

# Wait for the page to load
# time.sleep(5)

# Find the search bar element and send keys to it
# m = driver.find_element(By.ID, "APjFqb")
# m.send_keys("selenium")
# m.send_keys(Keys.ENTER)



# driver.find_element(By.XPATH,"//a[normalize-space()='Downloads']").click()




# Wait for a few seconds to see the result
# time.sleep(2)

# Close the browser
# driver.quit()

#ANNALECT
# main_link = driver.find_element(By.ID, "APjFqb").send_keys("annalect",Keys.ENTER)
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(2)
# driver.find_element(By.XPATH,"//h3[normalize-space()='Annalect India (@annalectindia)']").click()
# time.sleep(5)

#version 2
# a = driver.find_element(By.XPATH,"//*[contains(text(),'Working at Annalect')]")
# time.sleep(3)
# driver.execute_script("arguments[0].scrollIntoView(true);",a) #---scrolling into a specific element
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[contains(text(),'Annalect India (@annalectindia)')]").click()
# time.sleep(4)


#PIM - 24445 - SCRATCH

#WEBTABLE
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# allrows = driver.find_elements(By.XPATH,"(//table[@id = 'product'])[1]//tbody/tr/td")
# to print all the rows and columns
# for i in allrows:
#     print(i.text)

# to print specific element
# for i in allrows:
#     if i.text.__contains__(("JMETER")):
#         print(i.text)

#version 2
# for i in allrows:
#      if i.text.__contains__(("JMETER")):
#         nextvalue = i.find_element(By.XPATH,"./following-sibling::td")
#         print(nextvalue.text)

#version 3
# for i in allrows:
#      if i.text.__contains__(("JMETER")):
#         nextvalue = i.find_element(By.XPATH,"./preceding-sibling::td")
#         print(nextvalue.text)

#for 2nd table
# a = driver.find_elements(By.XPATH, "(//table[@id='product'])[2]//tbody/tr/td")

# Loop through each cell and check if it contains the text "Postman"
# for i in a:
#     if "Postman" in i.text:  # Check if the cell text contains "Postman"
#         # Find the next sibling cell and print its text
#         next_cell = i.find_element(By.XPATH, "./following-sibling::td")
#         print(next_cell.text)
#
#         # Find the previous sibling cell and print its text
#         previous_cell = i.find_element(By.XPATH, "./preceding-sibling::td")
#         print(previous_cell.text)