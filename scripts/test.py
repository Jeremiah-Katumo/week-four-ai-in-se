from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Setup 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://localhost:8501") # The url for the running streamlit app

# Wait for app to load for 5 seconds
time.sleep(5)

# Upload image (optional)
try:
    image_input = driver.find_element(By.XPATH, '//input[@type="file" and @accept=".jpg,.png"]')
    image_input.send_keys(os.path.abspath("validate_feature.jpg"))
    # The os.path.abspath() is used to convert the relative file path to an absolute one, ensuring 
    # that the browser can correctly locate the file on the system regardless of the current working directory.
    # Every browser require an absolute path when simulating file uploads throgh Selenium.
    # send_keys is being used to set the value of a file input, which is the standard way to automate file uploads in Selenium.
    print("✅ Image uploaded.")
    time.sleep(2)
except Exception:
    print("⚠️ Image upload skipped or input not found.")

# Upload CSV
try:
    csv_inputs = driver.find_elements(By.XPATH, '//input[@type="file"]')
    if len(csv_inputs) < 2:
        raise Exception("Not enough file input fields found.")

    csv_input = csv_inputs[-1]  # Second uploader is likely for CSV
    csv_input.send_keys(os.path.abspath("validate_feature.csv"))
    print("✅ CSV uploaded.")
    time.sleep(5)

    # Check result: verify if content has appeared on the page after uploading the csv file
    page_text = driver.page_source  # return the page html as a string, which can then be searched or parsed in Python
    if "Prediction" in page_text or "🧠 Prediction" in page_text:
        print("✅ Prediction displayed successfully.")
    else:
        print("❌ Prediction failed or not found.")

except Exception as e:
    print("❌ CSV upload failed:", e)

# Finish
driver.quit()
