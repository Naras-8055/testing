from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Amazon's URL
driver.get("https://www.amazon.com")

# Wait for a few seconds to observe the result
driver.implicitly_wait(60)

# Close the browser
driver.quit()