# Sentiment Analysis Web App

## Project Overview
This is a simple web-based Sentiment Analysis application built using **Python** and **Flask**.  
The app analyzes user-entered text and classifies it as **Positive**, **Negative**, or **Neutral**.

It also provides:
- Polarity score
- Subjectivity score
- Emoji-based sentiment output

---

## Features
- Clean and modern user interface
- Real-time sentiment analysis
- Emoji-based result display
- Reset button for new inputs
- Built using Flask and TextBlob

---

## Technologies Used
- Python
- Flask
- TextBlob
- HTML
- CSS

---

## Project Structure
Sentiment_Analysis_App/
│
├── app.py
├── requirements.txt
├── README.md
├── static/
│ └── style.css
└── templates/
└── index.html


---

## Installation & Setup

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/sentiment-analysis.git
cd sentiment-analysis
Step 2: Create virtual environment
python -m venv venv
Activate it:

Windows

venv\Scripts\activate
Mac/Linux

source venv/bin/activate
Step 3: Install dependencies
pip install -r requirements.txt
Step 4: Run the application
python app.py
Open browser and go to:

http://127.0.0.1:5000
How It Works
User enters text.

Flask sends text to TextBlob.

TextBlob calculates:

Polarity (positive/negative)

Subjectivity (opinion/fact)

Result is displayed with emoji.

Example Outputs
Text	Sentiment
I am very happy	😊 Positive
This is bad	😢 Negative
It is a table	😐 Neutral
Author
Manoj Kumar
