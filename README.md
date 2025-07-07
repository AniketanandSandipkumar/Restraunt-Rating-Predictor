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

##🗂️ Project Structure

graphql
Copy
Edit
├── app.py                  # Streamlit frontend interface
├── firstI.ipynb            # Notebook with EDA + model training
├── Dataset .csv            # Raw dataset
├── randomreg.pkl           # Trained Random Forest model
├── README.md               # Project documentation (this file)

##📦 Requirements

Python 3.7+
pandas
numpy
scikit-learn
streamlit
pickle

##📈 Example Output
yaml
Copy
Edit
Input:
- Location: Connaught Place
- Cuisine: North Indian
- Votes: 320
- Latitude/Longitude: 28.633, 77.219
- Current Rating: 3.8

## Output:
✅ Predicted Rating: 4.10 / 5

##📚 Learnings & Takeaways
1.Real-world data wrangling and cleaning
2.Encoding and feature selection for categorical data
3.Model selection and hyperparameter tuning
4.Deployment using Streamlit
5.Building intuitive interfaces for non-technical users

##🚀 Future Improvements
1.Support for real-time location detection via APIs
2.Inclusion of more advanced models like XGBoost or deep learning
3.Use of NLP on review texts (if available)

##🤝 Contributing
Pull requests and suggestions are welcome. For major changes, please open an issue first to discuss what you would like to change.

##📬 Contact
Author: Aniketanand Sandipkumar
📧 [Email-Id](aniketanand2712@gmail.com)
🔗 [LinkedIn](www.linkedin.com/in/aniketanand-sandipkumar-8475ab258)
