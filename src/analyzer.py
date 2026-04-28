import pandas as pd
from textblob import TextBlob
import sys
import os


def get_sentiment(text):
    """
    Analyzes text and returns a score:
    Positive (>0), Neutral (0), Negative (<0)
    """
    if not isinstance(text, str):
        return 0.0
    return TextBlob(text).sentiment.polarity


def process_reviews(df, text_column):
    """
    Adds sentiment scores and labels to the dataframe.
    """
    print(f"⏳ Analyzing {len(df)} reviews...")

    # Calculate score
    df['sentiment_score'] = df[text_column].apply(get_sentiment)

    # Create labels
    df['sentiment_label'] = df['sentiment_score'].apply(
        lambda x: 'Positive' if x > 0.1 else ('Negative' if x < -0.1 else 'Neutral')
    )

    print("✅ Analysis complete.")
    return df