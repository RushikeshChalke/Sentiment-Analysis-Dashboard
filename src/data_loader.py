import pandas as pd
import os

def load_sample_data():
    """
    Downloads data from URL.
    Cloud-safe version (no SSL bypass needed on Streamlit Cloud).
    """
    data_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 'data'
    )
    file_path = os.path.join(data_dir, 'reviews.csv')

    # If file exists locally, use it
    if os.path.exists(file_path):
        print("✅ Dataset already exists.")
        return pd.read_csv(file_path)

    # Otherwise download from URL
    print("⏳ Downloading data...")
    url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/sms.tsv"

    try:
        df = pd.read_csv(url, sep='\t', names=['label', 'message'])
        os.makedirs(data_dir, exist_ok=True)
        df.to_csv(file_path, index=False)
        print("✅ Downloaded successfully.")
        return df
    except Exception as e:
        print(f"❌ Download failed: {e}")
        # Last resort: try reading directly without saving
        try:
            df = pd.read_csv(url, sep='\t', names=['label', 'message'])
            return df
        except Exception as e2:
            print(f"❌ All attempts failed: {e2}")
            return None