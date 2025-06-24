# AI in Software Engineering

## Tasks for Week 4

1. Task 1: AI-Powered Code Completion - ( Naomi Wairimu and Faith Wafula )
2. Task 2: Automated Testing with AI - ( Obondo Patrick, Pharix Eloga )
3. Task 3: Predictive Analytics – Resource Allocation - ( Jeremiah Katumo )

# General Description

This repository contains code, notebooks, and scripts for exploring the application of artificial intelligence in software engineering, with a focus on predictive analysis using machine learning. The main example is a breast cancer classifier built with scikit-learn and Streamlit, accompanied by Jupyter notebooks for data exploration and model development, and automated tests using Selenium.

## Directory Structure

- **notebooks/**  
  Contains Jupyter notebooks for data analysis, preprocessing, model training, and evaluation.
  - `predictive_analysis.ipynb`: Main notebook for breast cancer data analysis and modeling.
  - `README.md`: Documentation for the notebooks directory.

- **scripts/**  
  Contains application and test scripts.
  - `app.py`: Streamlit web app for uploading data and getting predictions from a trained model.
  - `test.py`: Selenium-based automated test for the web app.

- **datasets/**  
  Contains datasets used in the notebooks and app.
  - `breast_cancer.csv`: Breast cancer dataset (features and labels).

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd week-four-ai-in-se
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
Or, manually install the main packages:
```bash
pip install streamlit scikit-learn pandas numpy matplotlib seaborn pyjanitor pillow selenium jupyter
```

### 4. Run the Jupyter Notebook

```bash
cd notebooks
jupyter notebook
```
Open `predictive_analysis.ipynb` in your browser.

### 5. Run the Streamlit App

```bash
cd scripts
streamlit run app.py
```
Visit [http://localhost:8501](http://localhost:8501) in your browser.

### 6. Run Automated Tests

Make sure the Streamlit app is running, then in another terminal:

```bash
cd scripts
python test.py
```

## Notes

- The app expects a CSV file with 30 columns (no header), matching the features of the breast cancer dataset.
- The image upload in the app is optional and for context only.
- The Selenium test requires Chrome and ChromeDriver installed and available in your PATH.
- All code is for educational and demonstration purposes.
