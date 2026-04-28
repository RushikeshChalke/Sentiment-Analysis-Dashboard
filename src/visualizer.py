from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os


def generate_wordcloud(df, label, filename):
    """
    Creates a word cloud for a specific sentiment label and saves it.
    """
    # Filter text by label
    text = " ".join(review for review in df[df['sentiment_label'] == label].message)

    if not text.strip():
        print(f"⚠️ No text found for label: {label}")
        return

    # Generate Cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='magma' if label == 'Negative' else 'viridis'
    ).generate(text)

    # Save it
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'outputs', filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(f"Top Words in {label} Messages")
    plt.savefig(output_path)
    plt.close()

    print(f"✅ {label} Word Cloud saved to: outputs/{filename}")