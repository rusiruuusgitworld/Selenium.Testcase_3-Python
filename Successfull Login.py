from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver (automatically downloads the correct driver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the login page
driver.get("https://www.saucedemo.com/")

# Locate the username and password fields and login button
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Enter the username and password
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

# Click the login button
login_button.click()

# Wait for the new page to load
time.sleep(10)

# Verify successful login by checking the presence of a specific element on the landing page
try:
    inventory_container = driver.find_element(By.ID, "inventory_container")
    print("Login successful.")
except:
    print("Login failed.")

# Close the browser
driver.quit()



