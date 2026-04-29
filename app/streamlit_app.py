import streamlit as st
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

# Path setup
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import load_sample_data
from src.analyzer import process_reviews, get_sentiment

# Page Config
st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="🗣️")

st.title("🗣️ AI Sentiment & Customer Voice Dashboard")
st.markdown("---")

# 1. Sidebar - Data Loading
st.sidebar.header("Data Controls")
if st.sidebar.button("Reload Data"):
    st.cache_data.clear()

# 2. Main Analytics
with st.spinner("Analyzing Customer Feedback..."):
    df = load_sample_data()
    if df is None:
        st.error("Failed to load data. Please refresh the page.")
        st.stop()

    df = process_reviews(df.head(500), 'message')

# Top Row Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", len(df))
col2.metric("Angry Customers", len(df[df['sentiment_label']=='Negative']))
col3.metric("Happy Customers", len(df[df['sentiment_label']=='Positive']))

st.markdown("---")

# 3. Visuals - Pie Chart & Word Cloud
c1, c2 = st.columns(2)

with c1:
    st.subheader("Sentiment Distribution")
    fig, ax = plt.subplots()
    df['sentiment_label'].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%',
        colors=['#66b3ff','#99ff99','#ff9999'],
        ax=ax
    )
    st.pyplot(fig)

with c2:
    st.subheader("Negative Word Cloud")
    cloud_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'outputs', 'negative_words.png')
    if os.path.exists(cloud_path):
        st.image(cloud_path)
    else:
        st.warning("Run 'run_analysis.py' first to generate clouds.")

st.markdown("---")

# 4. Interactive "Try the AI" section
st.subheader("🔮 Try the AI Brain")
user_input = st.text_area("Type a customer review here to test the AI:")

if user_input:
    score = get_sentiment(user_input)
    if score > 0.1:
        st.success(f"Positive Sentiment (Score: {score:.2f})")
    elif score < -0.1:
        st.error(f"Negative Sentiment (Score: {score:.2f})")
    else:
        st.warning(f"Neutral Sentiment (Score: {score:.2f})")

st.markdown("---")

# 5. The Feedback Table
st.subheader("🔍 Deep Dive: Negative Feedback")
neg_df = df[df['sentiment_label']=='Negative'][['message', 'sentiment_score']]
st.dataframe(neg_df, use_container_width=True)