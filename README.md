# 📊 Customer Feedback Analysis

A simple web application built with **Streamlit, MySQL, and Python** for collecting and analyzing customer feedback.

## 🌟 Features
✅ Submit feedback through a form  
✅ Perform **Sentiment Analysis** (Positive, Negative, Neutral)  
✅ Display feedback with **bar charts** and **word cloud**  
✅ Store feedback in **MySQL database**  

## 🛠️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python  
- **Database:** MySQL  
- **NLP:** TextBlob, NLTK  
- **Visualization:** Matplotlib, Seaborn, WordCloud  

## 🚀 Setup Instructions

### 1️⃣ Install Dependencies
Run the following command:
```bash
pip install -r requirements.txt

2️⃣ Setup MySQL Database
Run these SQL commands:

sql
Copy
Edit
CREATE DATABASE feedback_db;
USE feedback_db;
CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    feedback TEXT,
    sentiment VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

3️⃣ Run the Application
Start the Streamlit app:

bash
Copy
Edit
streamlit run app.py

📌 Future Enhancements
Add Admin Dashboard to view feedback trends
Integrate Machine Learning Model for better sentiment analysis
