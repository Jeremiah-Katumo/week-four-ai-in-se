# Predictive Analysis Notebook

This directory contains a Jupyter Notebook for predictive analysis on breast cancer data, along with supporting files and datasets. The workflow demonstrates data cleaning, preprocessing, exploratory data analysis, and building a machine learning model using a Random Forest classifier.

## Files

- **predictive_analysis.ipynb**  
  The main Jupyter Notebook. It walks through the process of loading the breast cancer dataset, cleaning and preparing the data, performing exploratory data analysis (EDA), building preprocessing pipelines, training a Random Forest classifier, evaluating its performance, and visualizing results such as the confusion matrix and a sample decision tree.

- **breast_cancer.csv** (in `../datasets/`)  
  The dataset used in the notebook. It contains features and labels for breast cancer diagnosis.

## Workflow Overview

1. **Data Loading and Cleaning:**  
   The notebook loads the breast cancer dataset, cleans column names, encodes the diagnosis labels, and removes unnecessary columns.

2. **Exploratory Data Analysis (EDA):**  
   It checks for missing values, duplicates, and explores the distribution of features and target classes.

3. **Preprocessing:**  
   Numeric and categorical features are processed using pipelines with imputation and scaling/encoding as appropriate.

4. **Model Training:**  
   The data is split into training and test sets. A Random Forest classifier is trained on the training data.

5. **Evaluation:**  
   The model's accuracy, classification report, and confusion matrix are computed and visualized.

6. **Visualization:**  
   The notebook includes code to visualize a single decision tree from the trained random forest for interpretability.

## Usage

1. **Install Dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pandas numpy matplotlib seaborn scikit-learn pyjanitor jupyter
   ```

2. **Start Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

   Then open `predictive_analysis.ipynb` in your browser.

3. **Dataset**

   Ensure that `breast_cancer.csv` is available in the `../datasets/` directory relative to the notebook.

## Notes

- The notebook uses the `pyjanitor` library for convenient data cleaning.
- The Random Forest model is used for classification, but you can experiment with other models as well.
- Visualizations are created using Matplotlib and Seaborn.
- The notebook is intended for educational and demonstration purposes.
