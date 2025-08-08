# 🛡️ Website URL Safety Detection

A machine learning–powered website that classifies URLs as **phishing** or **legitimate** using a trained **Gradient Boosting Classifier**.

## 🔧 Features
- Real-time URL safety prediction via a Flask-based website.
- Trained on phishing datasets with features like:
  - IP address presence
  - SSL certificate status
  - URL length and token patterns
- Displays prediction result with confidence score.

## 🧠 Tech Stack
- Python
- Scikit-learn
- Flask
- Pandas
- HTML/CSS (for UI)

## 🚀 How It Works
1. User enters a URL on the website.
2. The system extracts features from the URL.
3. A Gradient Boosting model predicts whether the URL is **safe** ✅ or **phishing** 🚨.
4. The result and confidence score are shown on screen.

## ▶️ Getting Started
1. git clone https://github.com/yourusername/url-safety-detctor.git
2. cd url-safety-detector
3. pip install -r requirements.txt
4. python app.py
