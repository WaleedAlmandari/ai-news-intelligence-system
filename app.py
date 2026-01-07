from flask import Flask, render_template, request, jsonify
import joblib
import spacy
import contractions
import random

app = Flask(__name__)

#1. Load Models
print("Loading system models...")
try:
    model = joblib.load('news_classifier_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    nlp = spacy.load("en_core_web_sm", disable=['ner', 'parser'])
    print("All models loaded successfully!")
except Exception as e:
    print(f"Error: {e}")

#2. Preprocessing
def preprocess_text(text):
    try:
        text = contractions.fix(text)
    except:
        pass
    doc = nlp(text)
    clean_tokens = [token.lemma_.lower() for token in doc 
                    if not token.is_stop and not token.is_punct and not token.like_num]
    return " ".join(clean_tokens)

#3.Chatbot Logic
def get_bot_response(user_message):
    msg = user_message.lower()
    
    responses = {
        'greeting': [
            "Hello! I am Isaac, your AI Assistant. How can I help you classify news today?",
            "Hi there! Ready to analyze some data? Ask me anything about the project.",
            "Greetings! I'm online and ready."
        ],
        'team': [
            "This system was built by Group Isaac Newton: Husam, Waleed, Osaid, and Yaseen.",
            "Our team consists of four developers: Husam, Waleed, Osaid, and Yaseen.",
            "Credits go to Group Isaac Newton members."
        ],
        'accuracy': [
            "Our Logistic Regression model achieves <b>91% accuracy</b> on unseen test data.",
            "We achieved approximately <b>91% precision</b>. It's quite reliable.",
            "The model is correct 9 times out of 10 (<b>91% Accuracy</b>) based on our testing."
        ],
        'dashboard': [
            "You can explore word clouds and charts on our <a href='/dashboard' target='_blank'>Dashboard</a>.",
            "Visualizations are available on the <a href='/dashboard' target='_blank'>Insights Page</a>."
        ],
        'algorithm': [
            "We use <b>TF-IDF</b> (Term Frequency-Inverse Document Frequency) to convert text into numbers, and <b>Logistic Regression</b> to classify it.",
            "The magic happens via <b>Logistic Regression</b>! It's a robust algorithm trained on 120,000 articles processed with <b>TF-IDF</b> (5000 features).",
            "Technically: 1. Cleaning (spaCy) -> 2. Vectorization (TF-IDF) -> 3. Classification (Logistic Regression)."
        ],
        'project_info': [
            "This is the <b>Isaac Newton News Portal</b>. We use AI to categorize news articles automatically.",
            "It's an AI project designed to classify text into World, Sports, Business, or Tech categories."
        ],
        'fallback': [
            "I'm still learning! Ask me about 'Algorithm', 'Accuracy', or 'Team'.",
            "I didn't quite catch that. Try asking: 'What algorithm is used?'"
        ]
    }

    # Logic
    if any(w in msg for w in ["hi", "hello", "hey"]):
        return random.choice(responses['greeting'])
    
    elif any(w in msg for w in ["team", "member", "created", "who"]):
        return random.choice(responses['team'])
    
    elif any(w in msg for w in ["accuracy", "performance", "precision"]):
        return random.choice(responses['accuracy'])
    
    elif any(w in msg for w in ["data", "dashboard", "chart", "graph"]):
        return random.choice(responses['dashboard'])
    
    elif any(w in msg for w in ["algorithm", "model", "method", "technique", "tf-idf", "regression", "how it works"]):
        return random.choice(responses['algorithm'])
        
    elif any(w in msg for w in ["project", "about", "system"]):
        return random.choice(responses['project_info'])
        
    else:
        return random.choice(responses['fallback'])

#4. Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news_text']
        clean_text = preprocess_text(news_text)
        vectorized_text = vectorizer.transform([clean_text])
        prediction = model.predict(vectorized_text)[0]
        return render_template('index.html', prediction_text=prediction, original_text=news_text)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['msg']
    response = get_bot_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)