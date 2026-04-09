import pandas as pd
import json
import os

# Constants
INPUT_FILE = "data/hacker_news.json"
OUTPUT_CSV = "data/cleaned_trends.csv"

def clean_and_convert():
    # 1. Load the JSON file
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found. Please run Task 1 first.")
        return

    with open(INPUT_FILE, "r") as f:
        data = json.load(f)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # 2. Cleaning Data
    # Remove any duplicate IDs
    df.drop_duplicates(subset="id", keep="first", inplace=True)
    
    # Fill missing URLs with 'N/A'
    df["url"] = df["url"].fillna("N/A")
    
    # Ensure numerical fields are integers (handle NaNs if any)
    df["score"] = df["score"].fillna(0).astype(int)
    df["descendants"] = df["descendants"].fillna(0).astype(int)
    
    # Optional: Convert Unix timestamp to readable date
    df["time"] = pd.to_datetime(df["time"], unit='s')
    
    # 3. Save as CSV
    df.to_csv(OUTPUT_CSV, index=False)
    
    print(f"Cleaned {len(df)} stories and saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    clean_and_convert()
