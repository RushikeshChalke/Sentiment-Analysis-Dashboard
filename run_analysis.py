import sys
import os

root_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, root_path)

from src.data_loader import load_sample_data
from src.analyzer import process_reviews
from src.visualizer import generate_wordcloud


def main():
    print("=" * 50)
    print("   SENTIMENT ANALYSIS PIPELINE")
    print("=" * 50)

    # 1. Load & Process
    df = load_sample_data()
    if df is not None:
        text_col = 'message'
        result_df = process_reviews(df.head(500), text_col)

        # 2. Generate Visuals
        print("\n🎨 GENERATING VISUAL REPORTS...")
        generate_wordcloud(result_df, 'Negative', 'negative_words.png')
        generate_wordcloud(result_df, 'Positive', 'positive_words.png')

        # 3. Final Summary
        print("\n✅ PIPELINE COMPLETE")
        print(f"   Negative reviews caught: {len(result_df[result_df['sentiment_label'] == 'Negative'])}")
        print("   Check 'outputs/' folder for Word Clouds.")


if __name__ == "__main__":
    main()