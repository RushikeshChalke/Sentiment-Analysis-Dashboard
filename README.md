# 🗣️ AI Customer Sentiment & Voice Dashboard
> An NLP-powered tool that reads customer reviews and tells brands exactly what people love and hate about their products.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TextBlob](https://img.shields.io/badge/NLP-TextBlob-green)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)

## 🔗 Live Demo
👉 [Click here to try the live app](PASTE_YOUR_STREAMLIT_URL_HERE)

## 🏢 Business Problem
Founders are drowning in customer feedback.
They get hundreds of reviews every day but have no way to:
- Know the overall "mood" of their customers
- Find the hidden complaints inside 4-star reviews
- Identify which words keep appearing in angry feedback

So they guess. And guessing costs money.

## 🚀 The Solution
An AI tool that reads every single review, detects the emotion
behind it, and summarizes thousands of sentences into one screen.

### What It Does:
- **Sentiment Scoring:** Labels every message as Positive, Negative, or Neutral
- **Word Cloud:** Visually shows the most common words in angry reviews
- **Real-Time Testing:** Type any sentence and see how the AI labels it instantly
- **Deep Dive Table:** Shows every negative review in one place for action

## 💰 Business Impact
- Identified **10% of customers** expressing negative sentiment
- Found specific "Pain Point" words without reading a single review manually
- Saves founders **hours of manual review reading** every week

## 🛠️ Tech Stack
- **NLP Engine:** TextBlob (Polarity & Subjectivity Analysis)
- **Visualization:** WordCloud, Matplotlib
- **Dashboard:** Streamlit
- **Architecture:** Modular, config-driven pipeline

## 📦 Project Structure
```text
Sentiment_Analysis_Project/
├── app/               → Streamlit Dashboard
├── config/            → Global Settings
├── src/               → Modular Scripts
│   ├── data_loader.py → Load data
│   ├── analyzer.py    → Sentiment engine
│   └── visualizer.py  → Word cloud generator
├── main.py            → Single entry point
└── requirements.txt   → Dependencies