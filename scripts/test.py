from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# === Setup ===
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://localhost:8501")

# === Wait for app to load ===
time.sleep(5)

# === Upload image (optional) ===
try:
    image_input = driver.find_element(By.XPATH, '//input[@type="file" and @accept=".jpg,.png"]')
    image_input.send_keys(os.path.abspath("validate_feature.jpg"))
    print("✅ Image uploaded.")
    time.sleep(2)
except Exception:
    print("⚠️ Image upload skipped or input not found.")

# === Upload CSV ===
try:
    csv_inputs = driver.find_elements(By.XPATH, '//input[@type="file"]')
    if len(csv_inputs) < 2:
        raise Exception("Not enough file input fields found.")

    csv_input = csv_inputs[-1]  # Second uploader is likely for CSV
    csv_input.send_keys(os.path.abspath("validate_feature.csv"))
    print("✅ CSV uploaded.")
    time.sleep(5)

    # Check result
    page_text = driver.page_source
    if "Prediction" in page_text or "🧠 Prediction" in page_text:
        print("✅ Prediction displayed successfully.")
    else:
        print("❌ Prediction failed or not found.")

except Exception as e:
    print("❌ CSV upload failed:", e)

# === Finish ===
driver.quit()
