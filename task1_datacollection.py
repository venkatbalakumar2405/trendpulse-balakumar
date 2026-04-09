import requests, json, os

def get_category(title):
    title = title.lower()
    if any(word in title for word in ['ai', 'gpt', 'ml', 'neural']): return 'AI/ML'
    if any(word in title for word in ['web', 'js', 'react', 'python']): return 'Dev'
    if any(word in title for word in ['startup', 'business', 'vc']): return 'Business'
    return 'General'

def fetch_data():
    ids = requests.get("https://firebaseio.com").json()[:100]
    stories = []
    for sid in ids:
        item = requests.get(f"https://firebaseio.com{sid}.json").json()
        if item and item.get("type") == "story":
            stories.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "category": get_category(item.get("title", "")),
                "score": item.get("score", 0),
                "author": item.get("by"),
                "time": item.get("time"),
                "url": item.get("url", "N/A")
            })
    
    os.makedirs("data", exist_ok=True)
    with open("data/raw_trends.json", "w") as f:
        json.dump(stories, f, indent=4)
    print("Task 1: Data collected.")

if __name__ == "__main__": fetch_data()
