from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver (automatically downloads the correct driver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the login page
    driver.get("https://www.saucedemo.com/")

    # Locate the username, password fields, and login button
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Enter the username and password
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    # Click the login button
    login_button.click()

    # Wait for the new page to load
    time.sleep(2)

    # Add the first product to the cart
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()

    # Click on the shopping cart icon
    cart_icon = driver.find_element(By.ID, "shopping_cart_container")
    cart_icon.click()

    # Wait for the cart page to load
    time.sleep(2)

    # Click the checkout button
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Wait for the checkout page to load
    time.sleep(2)

    # Fill in the checkout information
    first_name_field = driver.find_element(By.ID, "first-name")
    last_name_field = driver.find_element(By.ID, "last-name")
    postal_code_field = driver.find_element(By.ID, "postal-code")
    continue_button = driver.find_element(By.ID, "continue")

    first_name_field.send_keys("Rusiru")
    last_name_field.send_keys("Ediriweera")
    postal_code_field.send_keys("11300")

    # Click the continue button
    continue_button.click()

    # Wait for the next page to load
    time.sleep(2)

    # Click the finish button to complete the checkout
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()

    # Wait for the success page to load
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
