import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.52 Safari/537.36")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open Naukri login page
driver.get("https://www.naukri.com/nlogin/login")

# Fetch credentials from environment variables
username = os.getenv("NAUKRI_USERNAME")
password = os.getenv("NAUKRI_PASSWORD")

# Enter username and password
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "usernameField"))).send_keys(username)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "passwordField"))).send_keys(password)

# Click login button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))).click()

# Verify login success
WebDriverWait(driver, 30).until(EC.url_contains("dashboard"))
logger.info("Logged in successfully!")

# Close the browser
driver.quit()