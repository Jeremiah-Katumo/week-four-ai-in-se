# Breast Cancer Classifier Web App

This directory contains a Streamlit web application and related scripts for classifying breast cancer data using a Random Forest classifier. The app allows users to upload a CSV file containing 30 feature values and (optionally) an image for context. The model predicts whether the input data indicates a malignant or benign tumor.

## Files

- **app.py**  
  The main Streamlit application. It loads and trains a Random Forest classifier on the breast cancer dataset from scikit-learn, then provides a web interface for users to upload feature data and receive predictions.

- **test.py**  
  An automated Selenium test script that simulates user interactions with the web app. It uploads an image and a CSV file, then checks if the prediction result is displayed.

## Usage

### 1. Install Dependencies

Create a virtual environment and install the required packages:

```bash
python3 -m venv venv
source venv/bin/activate
pip install streamlit scikit-learn pandas numpy pillow selenium
```

You will also need [Google Chrome](https://www.google.com/chrome/) and [ChromeDriver](https://chromedriver.chromium.org/) for Selenium tests.

### 2. Run the App

Start the Streamlit app:

```bash
streamlit run app.py
```

Open your browser to [http://localhost:8501](http://localhost:8501).

### 3. Using the App

- **Upload an Image (optional):**  
  You can upload a `.jpg` or `.png` image for context.
- **Upload a CSV File:**  
  Upload a CSV file with 30 columns (no header), each row representing a sample to classify. The app will display the data and show the prediction.

### 4. Automated Testing

To run the Selenium test (make sure the app is running):

```bash
python test.py
```

This will simulate uploading files and check if the prediction appears.

## Notes

- The CSV file must have exactly 30 columns per row, matching the features expected by the model.
- The app uses the built-in breast cancer dataset from scikit-learn.
- The image upload is optional and does not affect the prediction.

## Example CSV Row

```
17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189
```