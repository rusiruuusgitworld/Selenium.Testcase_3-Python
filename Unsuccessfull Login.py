from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver (automatically downloads the correct driver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the login page
driver.get("https://www.saucedemo.com/")

# Locate the login button
login_button = driver.find_element(By.ID, "login-button")

# Click the login button with empty credentials
login_button.click()

# Wait for the error message to load
time.sleep(20)

# Verify unsuccessful login by checking the presence of an error message
try:
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if "Username is required" in error_message.text:
        print("Unsuccessful login verified with empty credentials.")
    else:
        print("Unexpected error message.")
except:
    print("Error message not found. Test failed.")

# Close the browser
driver.quit()
