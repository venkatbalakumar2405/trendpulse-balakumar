import pandas as pd

def process_data():
    df = pd.read_json("data/raw_trends.json")
    df.drop_duplicates(subset="id", inplace=True)
    df.to_csv("data/clean_trends.csv", index=False)
    # Also save a JSON version for your Task 3 code snippet
    df.to_json("data/clean_trends.json", orient="records", indent=4)
    print("Task 2: Data cleaned and saved to CSV/JSON.")

if __name__ == "__main__": process_data()
