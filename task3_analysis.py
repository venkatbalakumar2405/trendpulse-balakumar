import json
from collections import Counter

INPUT_FILE = "data/clean_trends.json"

def analyze():

    with open(INPUT_FILE) as f:
        stories = json.load(f)

    categories = [story["category"] for story in stories]

    counter = Counter(categories)

    print("\nTrending Categories\n")

    for category, count in counter.items():
        print(category, ":", count)

    return counter


if __name__ == "__main__":
    analyze()