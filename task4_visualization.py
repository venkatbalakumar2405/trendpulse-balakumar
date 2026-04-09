import json
import matplotlib.pyplot as plt
from collections import Counter
import os

INPUT_FILE = "data/clean_trends.json"

def visualize():

    with open(INPUT_FILE) as f:
        stories = json.load(f)

    categories = [story["category"] for story in stories]

    counter = Counter(categories)

    names = list(counter.keys())
    values = list(counter.values())

    os.makedirs("charts", exist_ok=True)

    plt.figure(figsize=(8,6))
    plt.bar(names, values)

    plt.title("Trending Categories")
    plt.xlabel("Category")
    plt.ylabel("Number of Stories")

    plt.savefig("charts/category_chart.png")

    plt.show()

    print("Chart saved in charts/category_chart.png")


if __name__ == "__main__":
    visualize()