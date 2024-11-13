from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("First Name")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Last Name")

email_addr = driver.find_element(By.NAME, value="email")
email_addr.send_keys("Email@email.com")

sign_up = driver.find_element(By.CSS_SELECTOR, value="button")
sign_up.click()

# # Other solution
# input_element = driver.find_element(By.CSS_SELECTOR, value="input")
# input_element.send_keys("First Name", Keys.TAB, "Last Name", Keys.TAB, "Email@email.com", Keys.TAB, Keys.ENTER)

# driver.quit()
