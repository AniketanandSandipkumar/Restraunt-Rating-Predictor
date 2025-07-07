import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load trained model
with open("randomreg.pkl", "rb") as file:
    model = pickle.load(file)

# 🎨 Page Config
st.set_page_config(page_title="Restaurant Rating Predictor", page_icon="🍽️", layout="wide")

# 🖌️ Custom CSS Styling
st.markdown("""
    <style>
        body {background-color: #F4F6F6;}
        .stApp {background-color: #FFFFFF; border-radius: 15px; padding: 25px;}
        .title {color: #2C3E50; text-align: center; font-size: 42px; font-weight: 700; margin-bottom: 10px;}
        .subtitle {color:  #4A90E2; text-align: center; font-size: 18px; margin-bottom: 40px;}
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 10px;
            width: 100%;
        }
        .result {font-size: 22px; color: #2E8B57; font-weight: 600;}
        div[data-testid="stSelectbox"] label, 
        div[data-testid="stNumberInput"] label {
            font-size: 16px !important;
            font-weight: 600 !important;
            color: #333333 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 🔤 Title and Description
st.markdown("<p class='title'>🍽️ Restaurant Rating Predictor</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Predict how your restaurant will be rated based on its features like location, cuisine, and votes!</p>", unsafe_allow_html=True)

# 🧭 Sidebar Info
st.sidebar.header("📘 Model Information")
st.sidebar.info("""
- **Model Type:** Random Forest Regressor  
- **Goal:** Predict Aggregate Rating (out of 5)  
- **Input Features:** Location, Cuisines, Votes, and more  
""")

# 📊 Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("Dataset .csv")

df = load_data()

# Generate frequency mappings
cuisines_mapping = df['Cuisines'].value_counts().to_dict()
locality_mapping = df['Locality'].value_counts().to_dict()

# 👇 Input UI (Split into two columns for better layout)
col1, col2 = st.columns(2)

with col1:
    longitude = st.number_input("📍 Longitude", min_value=-157.948486, max_value=174.8320893, format="%.6f")
    selected_locality = st.selectbox("🏙️ Select Locality", ["Select"] + list(locality_mapping.keys()))
    votes = st.number_input("🗳️ Number of Votes", min_value=0, max_value=10000, step=1)

with col2:
    latitude = st.number_input("🌐 Latitude", min_value=-41.330428, max_value=55.97698, format="%.6f")
    selected_cuisine = st.selectbox("🍲 Select Cuisine", ["Select"] + list(cuisines_mapping.keys()))
    rating = st.number_input("⭐ Current Aggregate Rating", min_value=0.0, max_value=4.9, format="%.1f")

# 🧮 Prepare Frequency & Scaling
locality_freq = locality_mapping.get(selected_locality, 0)
cuisine_freq = cuisines_mapping.get(selected_cuisine, 0)

votes_scaler = StandardScaler()
votes_scaler.fit(df[['Votes']])
votes_scaled = votes_scaler.transform([[votes]])[0][0]

# 🚀 Predict Button
if st.button("✨ Predict Restaurant Rating"):
    try:
        input_data = np.array([[
            rating,
            votes_scaled,
            cuisine_freq,
            locality_freq,
            longitude,
            latitude
        ]])

        prediction = model.predict(input_data)
        st.success("✅ Prediction Successful!")

        st.markdown(f"<div class='result'>📊 Predicted Rating: <b>{prediction[0]:.2f} / 5</b></div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ An error occurred during prediction: {str(e)}")

