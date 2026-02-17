# 🧠 AI News Intelligence System

An end-to-end AI-powered web application that automatically classifies news articles into categories using Natural Language Processing (NLP) techniques.

## 🚀 Project Overview

This system uses TF-IDF for text vectorization and Logistic Regression for classification, achieving **91% accuracy** on unseen test data.

The application includes:
- 📰 Real-time news classification
- 🤖 Interactive AI chatbot assistant
- 📊 Data visualization dashboard
- 🧠 NLP preprocessing pipeline

---

## 🏗️ System Architecture

1. Text Preprocessing (spaCy + Lemmatization)
2. Feature Extraction (TF-IDF - 5000 features)
3. Classification (Logistic Regression)
4. Web Interface (Flask)

---

## 📂 Project Structure

ai-news-intelligence-system/
│
├── app.py # Flask application
├── news_model_training.ipynb # Model training notebook
├── requirements.txt # Dependencies
├── templates/ # HTML templates
├── static/ # Static assets
└── README.md


---

## 🧪 Model Performance

- Algorithm: Logistic Regression
- Vectorization: TF-IDF
- Accuracy: **91%**
- Dataset Size: ~120,000 articles

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/WaleedAlmandari/ai-news-intelligence-system.git
cd ai-news-intelligence-system


### 2️⃣ Install dependencies

pip install -r requirements.txt
python -m spacy download en_core_web_sm


### 3️⃣ Run the application

python app.py


Open in browser:
http://127.0.0.1:5000/


---

## 📊 Dashboard

The system includes an interactive dashboard for exploring insights and visual analytics.

---

## 🤖 Chatbot

The built-in chatbot can answer questions about:
- Team members
- Model accuracy
- Algorithms used
- Project information

---

## 👨‍💻 Developed By

Group Isaac Newton:
- Husam
- Waleed
- Osaid
- Yaseen

---

## 🎯 Future Improvements

- Deploy to cloud (Render / AWS)
- Add Deep Learning model (LSTM / BERT)
- Add confidence score to predictions
- Improve chatbot with NLP intent detection

---

## 📜 License

This project is developed for educational and portfolio purposes.
