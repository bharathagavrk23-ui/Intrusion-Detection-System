from flask import Flask, request, render_template
import joblib
from extractor.features import extract_features

app = Flask(__name__)

# Load pre-trained model
model = joblib.load("model/phishing_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        url = request.form['url']
        features = extract_features(url)
        prediction = model.predict([features])[0]
        proba = model.predict_proba([features])[0]

        result = {
            'url': url,
            'prediction': 'Phishing 🚨' if prediction == 1 else 'Legitimate ✅',
            'confidence': f"{round(max(proba)*100, 2)}%"
        }

        return render_template('result.html', result=result)

    except Exception as e:
        return render_template('result.html', result={'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
