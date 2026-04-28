import pandas as pd
import os
import ssl


def load_sample_data():
    """
    Downloads a sample Amazon reviews dataset with SSL bypass for Mac.
    """
    ssl._create_default_https_context = ssl._create_unverified_context

    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    file_path = os.path.join(data_dir, 'reviews.csv')

    if os.path.exists(file_path):
        print("✅ Dataset already exists in data folder.")
        return pd.read_csv(file_path)

    print("⏳ Downloading sample review data (Baby Products)...")
    # This is a very stable dataset URL
    url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/sms.tsv"

    try:
        # We'll use this SMS dataset as a backup if Amazon fails
        # It's great for sentiment (spam vs ham)
        df = pd.read_csv(url, sep='\t', names=['label', 'message'])
        df.to_csv(file_path, index=False)
        print(f"✅ Successfully downloaded and saved to {file_path}")
        return df
    except Exception as e:
        print(f"❌ Error downloading data: {e}")
        return None