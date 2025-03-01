from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(feedback_text):
    sentiment_score = TextBlob(feedback_text).sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"
