import json

INPUT_FILE = "data/trends_20260409.json"
OUTPUT_FILE = "data/clean_trends.json"

def clean_data():

    with open(INPUT_FILE) as f:
        stories = json.load(f)

    cleaned = []

    for story in stories:

        if story["title"] == "":
            continue

        if story["score"] < 5:
            continue

        cleaned.append(story)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(cleaned, f, indent=4)

    print("Cleaned records:", len(cleaned))


if __name__ == "__main__":
    clean_data()