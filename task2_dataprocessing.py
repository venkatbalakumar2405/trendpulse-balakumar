import json
import pandas as pd

INPUT_FILE = "data/trends_20260409.json"

def process_data():

    with open(INPUT_FILE, "r") as f:
        stories = json.load(f)

    df = pd.DataFrame(stories)

    print("\nDataset Preview\n")
    print(df.head())

    print("\nBasic Info\n")
    print(df.info())

    return df


if __name__ == "__main__":
    process_data()