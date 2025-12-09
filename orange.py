from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait for the page to load
time.sleep(3)

# Enter the username
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")

# Enter the password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

# Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for the dashboard to load
time.sleep(5)

# Click on the "My Info" tab
my_info_tab = driver.find_element(By.LINK_TEXT, "My Info")
my_info_tab.click()

# Wait for a few seconds to observe the result
time.sleep(5)

# Close the browser
driver.quit()