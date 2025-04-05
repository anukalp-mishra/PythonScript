from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up Chrome options for debugging
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.52 Safari/537.36")  # Custom User-Agent

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open Naukri login page
driver.get("https://www.naukri.com/nlogin/login")

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "usernameField")))

# Fetch credentials from environment variables
username = os.getenv("NAUKRI_USERNAME")
password = os.getenv("NAUKRI_PASSWORD")

# Ensure credentials are provided
if not username or not password:
    raise ValueError("Naukri credentials are not set in environment variables.")

# Wait for the username field to be clickable
try:
    username_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "usernameField"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", username_field)  # Scroll to the element
    username_field.send_keys(username)
    print("Entered username successfully!")
except Exception as e:
    print(f"Error interacting with username field: {e}")
    print("Element attributes for debugging:")
    element = driver.find_element(By.ID, "usernameField")

# Enter password and click login
try:
    password_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "passwordField"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", password_field)  # Scroll to the element
    password_field.send_keys(password)
    print("Entered password successfully!")
except Exception as e:
    print(f"Error interacting with password field: {e}")
    print("Element attributes for debugging:")
    element = driver.find_element(By.ID, "passwordField")

# Verify login success
try:
    WebDriverWait(driver, 30).until(EC.url_contains("dashboard"))
    print("Logged in successfully! Current URL:", driver.current_url)
except Exception as e:
    print(f"Error verifying login: {e}")
    print("Current URL:", driver.current_url)
    driver.quit()
    raise

# Navigate to the Profile Page
profile_url = "https://www.naukri.com/mnjuser/profile"
driver.get(profile_url)
print("Navigated to Profile Page. Current URL:", driver.current_url)

# Wait for the profile page to load
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='attachCV']")))
    print("Navigated to Profile Page!")
except Exception as e:
    print(f"Error navigating to Profile Page: {e}")
    print("Page source for debugging:")
    print(driver.page_source)
    driver.quit()
    raise

# Path to your new resume file
resume_path = os.path.join(os.getcwd(), "Anukalp-Resume.pdf")
if not os.path.exists(resume_path):
    raise FileNotFoundError(f"Resume file not found at path: {resume_path}")

# Find and upload resume
try:
    upload_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='attachCV']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", upload_button)
    upload_button.send_keys(resume_path)
    print("Resume uploaded successfully!")
except Exception as e:
    print(f"Error uploading resume: {e}")
    print("Page source for debugging:")
    print(driver.page_source)

# Close the browser
driver.quit()