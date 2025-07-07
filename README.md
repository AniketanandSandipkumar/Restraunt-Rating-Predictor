# 🍽️ Restaurant Rating Predictor ML Model

This project aims to predict restaurant ratings (on a scale of 0–5) based on various features such as location, cuisine type, user votes, and more. It leverages machine learning, specifically a **Random Forest Regressor**, and includes a user-friendly **Streamlit** web interface for interaction.

---

## 📌 Project Overview

The goal of this project is to build a predictive model that estimates a restaurant's rating based on publicly available features. This can be useful for:
- New restaurant owners estimating how their establishment might perform.
- Food delivery or aggregator platforms for ranking and recommendation.
- Data science learners looking to explore real-world regression problems.

---

## 🧠 Machine Learning Pipeline

### 📁 Dataset:
The dataset (`Dataset .csv`) includes key features:
- `Longitude`, `Latitude` – Geolocation of the restaurant  
- `Locality`, `Cuisines` – Categorical descriptors  
- `Votes` – Number of user reviews  
- `Aggregate Rating` – Target variable (continuous, range: 0 to 5)  

### 🧪 Model:
- **Algorithm:** Random Forest Regressor  
- **Preprocessing:**
  - Frequency encoding for `Locality` and `Cuisines`
  - Feature scaling for `Votes`
- **Evaluation:** Model trained and tested using standard train-test split with metrics like MAE and R² Score (check notebook for details).

### 🧾 Notebook:
- `firstI.ipynb` contains:
  - Exploratory Data Analysis (EDA)
  - Feature engineering
  - Model training and evaluation
  - Pickle export of the trained model

---

## 💻 Web App (Streamlit)

A fully interactive **Streamlit** app (`app.py`) is included for live rating prediction.

### 🔧 Features:
- Dropdowns for selecting locality and cuisine
- Sliders for entering geographical coordinates, number of votes, and current rating
- Real-time model prediction and display of predicted rating
- Styled interface using custom CSS
- Sidebar with model information

### 🧠 Input Parameters Used for Prediction:
- Aggregate Rating (current)
- Scaled Votes
- Cuisine Frequency
- Locality Frequency
- Longitude & Latitude

### ▶️ How to Run the App

```bash
# Step 1: Clone the repository
git clone https://github.com/your-username/restaurant-rating-predictor.git
cd restaurant-rating-predictor

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the Streamlit app
streamlit run app.py
