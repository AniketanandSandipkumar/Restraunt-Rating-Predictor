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
The dataset (Dataset .csv) includes key features:
- Longitude, Latitude – Geolocation of the restaurant  
- Locality, Cuisines – Categorical descriptors  
- Votes – Number of user reviews  
- Aggregate Rating – Target variable (continuous, range: 0 to 5)  

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

# Step 1: Clone the repository
git clone https://github.com/your-username/restaurant-rating-predictor.git
cd restaurant-rating-predictor

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the Streamlit app
streamlit run app.py

##🗂️ Project Structure:

-graphql
<br>
-Copy
<br>
-Edit
<br>
-├── app.py                    (Streamlit frontend interface)
<br>
-├── firstI.ipynb             (Notebook with EDA + model training)
<br>
-├── Dataset .csv             (Raw dataset)
<br>
-├── randomreg.pkl            (Trained Random Forest model)
<br>
-├── README.md                (Project documentation (this file))
<br>

##📦 Requirements:
<br>
-Python 3.7+ <br>
-pandas<br>
-numpy<br>
-scikit-learn<br>
-streamlit<br>
-pickle<br>

##📈 Example Output:
<br>
Input:<br>
- Location: Connaught Place<br>
- Cuisine: North Indian<br>
- Votes: 320<br>
- Latitude/Longitude: 28.633, 77.219<br>
- Current Rating: 3.8<br>

## Output:<br>
✅ Predicted Rating: 4.10 / 5

##📚 Learnings & Takeaways<br>
1.Real-world data wrangling and cleaning<br>
2.Encoding and feature selection for categorical data<br>
3.Model selection and hyperparameter tuning<br>
4.Deployment using Streamlit<br>
5.Building intuitive interfaces for non-technical users<br>

##🚀 Future Improvements<br>
1.Support for real-time location detection via APIs<br>
2.Inclusion of more advanced models like XGBoost or deep learning<br>
3.Use of NLP on review texts (if available)<br>

##🤝 Contributing<br>
Pull requests and suggestions are welcome. For major changes, please open an issue first to discuss what you would like to change.

##📬 Contact:<br>
-Author: Aniketanand Sandipkumar<br>
📧 [Email-Id](aniketanand2712@gmail.com)<br>
🔗 [LinkedIn](www.linkedin.com/in/aniketanand-sandipkumar-8475ab258)
