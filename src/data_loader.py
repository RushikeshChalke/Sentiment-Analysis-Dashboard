import pandas as pd
import os

def load_sample_data():
    """
    Loads sample text data.
    Uses a built-in dataset that works on any machine
    including Streamlit Cloud without any downloads.
    """
    print("⏳ Loading sample data...")

    # These are sample reviews built directly into the code
    # No download needed, works everywhere
    data = {
        'message': [
            "I absolutely love this product! Best purchase ever.",
            "Terrible quality. Broke after one day. Very disappointed.",
            "It is okay. Nothing special but does the job.",
            "Amazing! Exceeded all my expectations. Will buy again.",
            "Worst experience ever. Do not waste your money.",
            "Pretty good overall. Delivery was fast.",
            "Not worth the price. Very cheap material.",
            "Fantastic product. My whole family loves it.",
            "Returned it immediately. Complete waste of money.",
            "Decent product. Works as described.",
            "Absolutely brilliant. Five stars without hesitation.",
            "Stopped working after a week. Very frustrating.",
            "Good value for money. Happy with my purchase.",
            "Disappointing. Expected much better quality.",
            "Love it! Would highly recommend to everyone.",
            "Poor customer service and bad product quality.",
            "Exceeded my expectations. Really happy with this.",
            "Waste of money. Do not buy this product.",
            "Great product. Fast delivery. Will order again.",
			"Not impressed. Product looks nothing like the photos.",
            "Really satisfied with this purchase. Works perfectly.",
            "Broke on first use. Extremely disappointed.",
            "Good product but packaging was damaged on arrival.",
            "Incredible quality. Worth every penny.",
            "Terrible. Stopped working after 2 days.",
            "Very happy with this. Great value.",
            "Would not recommend. Very poor quality.",
            "Excellent product. Exactly as described.",
            "Not great. Expected better for the price.",
            "Super happy with my purchase. Will buy again.",
            "Arrived broken. Very upset with this purchase.",
            "Works perfectly. Very easy to use.",
            "Disappointed with the quality. Feels very cheap.",
            "Best product I have bought this year.",
            "Complete waste of money. Avoid this product.",
            "Very good quality. Happy with my purchase.",
            "Does not work as advertised. Very misleading.",
            "Outstanding quality. Highly recommended.",
            "Poor quality. Broke after first use.",
            "Really impressed with this product.",
            "Not what I expected. Very disappointed.",
            "Great value for money. Works perfectly.",
            "Stopped working immediately. Very frustrated.",
            "Brilliant product. Exceeded expectations.",
            "Terrible quality. Would not buy again.",
            "Very satisfied. Works exactly as described.",
            "Broken on arrival. Very poor packaging.",
            "Love this product. Worth every penny.",
            "Worst purchase I have ever made.",
            "Really good quality. Will recommend to friends.",
        ]
    }

    df = pd.DataFrame(data)
    print(f"✅ Loaded {len(df)} sample reviews.")
    return df