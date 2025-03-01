import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from database import fetch_feedback

# Generate Sentiment Distribution Chart
def plot_sentiment_distribution():
    feedback_data = fetch_feedback()
    df = pd.DataFrame(feedback_data)

    if not df.empty:
        plt.figure(figsize=(6, 4))
        sns.countplot(x=df["sentiment"], palette="coolwarm")
        plt.title("Feedback Sentiment Distribution")
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.show()

# Generate Word Cloud from Feedback
def plot_wordcloud():
    feedback_data = fetch_feedback()
    df = pd.DataFrame(feedback_data)

    if not df.empty:
        text = " ".join(df["feedback"])
        wordcloud = WordCloud(width=600, height=400, background_color="white").generate(text)

        plt.figure(figsize=(8, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Most Common Words in Feedback")
        plt.show()
