from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    polarity = 0.0
    subjectivity = 0.0
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "")

        if text.strip() != "":
            blob = TextBlob(text)

            # Sentiment scores
            polarity = round(blob.sentiment.polarity, 3)
            subjectivity = round(blob.sentiment.subjectivity, 3)

            # Sentiment classification
            if polarity > 0.1:
                sentiment = "Positive"
            elif polarity < -0.1:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

    return render_template(
        "index.html",
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=True)
