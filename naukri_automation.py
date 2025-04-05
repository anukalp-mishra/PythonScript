from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Custom User-Agent

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open Naukri login page
driver.get("https://www.naukri.com/nlogin/login")

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "usernameField")))

# Enter credentials (Replace with your details)
username = "anukalp.info@gmail.com"
password = "Loveami2k22@"

# Find username & password fields and enter values
driver.find_element(By.ID, "usernameField").send_keys(username)
driver.find_element(By.ID, "passwordField").send_keys(password)

# Click login button
driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

# Allow time for login
time.sleep(5)

print("Logged in successfully!")

# Navigate to the Profile Page
profile_url = "https://www.naukri.com/mnjuser/profile"
driver.get(profile_url)

# Wait for the profile page to load
time.sleep(5)

print("Navigated to Profile Page!")

import os

# Path to your new resume file (Change this to your actual resume path)
resume_path = "/Users/anukalp/Documents/MyData/Anukalp-Resume.pdf"

# Find and upload resume
upload_button = driver.find_element(By.XPATH, "//input[@id='attachCV']")
upload_button.send_keys(resume_path)

# Wait for upload to complete
time.sleep(5)

print("Resume uploaded successfully!")

# Close the browser
driver.quit()