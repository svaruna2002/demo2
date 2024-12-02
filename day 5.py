from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
#
# #scroll for table 2
# time.sleep(5)
# a = driver.find_element(By.XPATH, "//*[@class ='tableFixHead']/table/tbody/tr[6]/td[2]")
# time.sleep(5)
# driver.execute_script("arguments[0].scrollIntoView(true);", a)
# time.sleep(8)

#organge hrm -
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(5)
#
# driver.maximize_window()
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
#
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# time.sleep(5)
# actions = ActionChains(driver)
# admin1 = driver.find_element(By.LINK_TEXT, "Admin")
# actions.move_to_element(admin1).click().perform()
# time.sleep(5)
#
# user_man = driver.find_element(By.XPATH, "//span[text()='User Management ']")
# actions.move_to_element(user_man).click().perform()
# time.sleep(5)
#
# user_man = driver.find_element(By.XPATH, "//span[text()='Job ']")
# actions.move_to_element(user_man).click().perform()
# time.sleep(5)
#
# act = ActionChains(driver)
# rightclick = driver.find_element(By.LINK_TEXT,'Gmail')
# act.context_click(rightclick).perform()
# time.sleep(3)

#double click

#driver.get("https://demoqa.com/doubleClickBtn")
# doubleclick= driver.find_element(By.ID,"doubleClickBtn")
# act = ActionChains(driver)
# act.double_click(doubleclick).perform()


#drag & drop
# driver.get("https://demoqa.com/droppable")
# source = driver.find_element(By.ID,"draggable")
# destination = driver.find_element(By.ID,"droppable")
# act = ActionChains(driver)
#
# time.sleep(3)
# act.drag_and_drop(source,destination).perform()



#commands - different actions performed in selenium
#this will press the control button in the keyboard and press a - cant understand this quite yet
#act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).release().perform()
#act.key_down(Keys.CONTROL).send_keys("a+").key_up(Keys.CONTROL).perform()


#act.click_and_hold().release().perform()

# hover to sheety website and click on top
# version1 - working
# driver.execute_script("window.scrollTo(0,1300);")
#
# actions = ActionChains(driver)
# hover_element = driver.find_element(By.CLASS_NAME,"mouse-hover")
# time.sleep(3)
# actions.move_to_element(hover_element).perform()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,"a[href='#top']").click()
# time.sleep(5)

#version 2
# mh = driver.find_element(By.ID,'mousehover')
# click= driver.find_element(By.LINK_TEXT,'Top')
# time.sleep(5)
# driver.execute_script("window.scrollTo(0,1300);")
# act = ActionChains(driver)
# act.move_to_element().click(click).perform()
# time.sleep(8)

# to cross verify  - to check if it clicked on top
# actual = driver.current_url
# print(actual)
# expected = "#top"
#
# # assert actual in expected,"it is not same"
# # print("Top is in URL")
#
# assert actual.__contains__(expected)

#normal alert
# driver.get("https://demoqa.com/alerts")
# driver.find_element(By.ID, "alertButton").click()
# alert = driver.switch_to.alert
# alert.accept()
# driver.find_element(By.ID, "confirmButton").click()
# errormsg = alert.text
# print(errormsg)
# alert.dismiss()
# time.sleep(5)
#

# #prompt alert
# driver.find_element(By.ID, "promptButton").click()
# alert.send_keys("Sunil")
# alert.accept()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(5)
# alertyuy = driver.find_element(By.ID, "alertButton").click()
# time.sleep(3)
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
# time.sleep(5)

dtrx = driver.find_element(By.ID, "timerAlertButton").click()  #have to put variable for evrything
time.sleep(8)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(5)
#
# driver.find_element(By.ID, "confirmButton").click()
# time.sleep(3)
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
# alert.dismiss()
# time.sleep(5)
# #
# driver.find_element(By.ID, "promtButton").click()
# time.sleep(3)
# alert = driver.switch_to.alert
# alert.send_keys("Peter")
# print(alert.text)
# alert.accept()
# time.sleep(5)

