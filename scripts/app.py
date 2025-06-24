import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

# Load and train model
data = load_breast_cancer()
X, y = data.data, data.target
feature_names = data.feature_names

model = RandomForestClassifier()
model.fit(X, y)

st.title("🏥 Breast Cancer Classifier with CSV Upload")
st.write("Upload a CSV file with 30 feature values to classify. You can also upload an image for context.")

# Optional image upload
uploaded_image = st.file_uploader("Upload an optional image", type=["jpg", "png"])
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

# Upload CSV file with features
st.subheader("📄 Upload Feature CSV")
uploaded_csv = st.file_uploader("Upload a CSV file with 30 feature columns", type=["csv"])

if uploaded_csv:
    try:
        df = pd.read_csv(uploaded_csv, header=None)
        # Validation
        # If your CSV has a header and one row
        if df.shape[1] != 30:
            st.error(f"CSV should have 30 columns. You provided {df.shape[1]}.")
        elif df.shape[0] == 0:
            st.error("⚠️ CSV has no rows of data.")
        else:
            st.write("✅ CSV loaded:")
            st.dataframe(df)

            prediction = model.predict(df)[0]
            label = data.target_names[prediction]
            st.success(f"🧠 Prediction: **{label}**")
    except Exception as e:
        st.error(f"❌ Failed to read CSV: {e}")
