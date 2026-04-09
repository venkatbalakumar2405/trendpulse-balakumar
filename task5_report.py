import json

INPUT_FILE = "data/clean_trends.json"

def generate_report():

    with open(INPUT_FILE) as f:
        stories = json.load(f)

    print("\nTop 10 Trending Stories\n")

    for story in stories[:10]:

        print("Title:", story["title"])
        print("Category:", story["category"])
        print("Score:", story["score"])
        print("Comments:", story["num_comments"])
        print("Author:", story["author"])
        print("-"*40)


if __name__ == "__main__":
    generate_report()