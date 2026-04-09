import requests
import json
import os

# Constants
API_TOP_STORIES = "https://firebaseio.com"
API_ITEM_DETAIL = "https://firebaseio.com{}.json"
OUTPUT_DIR = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "hacker_news.json")

def fetch_hacker_news():
    # 1. Fetch from HackerNews API (8 Marks)
    # Get the list of top story IDs
    response = requests.get(API_TOP_STORIES)
    story_ids = response.json()
    
    stories = []
    # Loop until at least 100 stories are collected
    for sid in story_ids:
        if len(stories) >= 100:
            break
            
        item_res = requests.get(API_ITEM_DETAIL.format(sid))
        item_data = item_res.json()
        
        # Check if item exists and is a story
        if item_data and item_data.get("type") == "story":
            # 2. Extract required fields - 7 fields (7 Marks)
            story_extracted = {
                "id": item_data.get("id"),
                "title": item_data.get("title"),
                "url": item_data.get("url", ""),
                "score": item_data.get("score"),
                "author": item_data.get("by"),
                "time": item_data.get("time"),
                "descendants": item_data.get("descendants", 0) # Comment count
            }
            stories.append(story_extracted)

    # 3. Save to JSON file in data/ folder (5 Marks)
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    with open(OUTPUT_FILE, "w") as f:
        json.dump(stories, f, indent=4)
    
    print(f"Successfully saved {len(stories)} stories to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_hacker_news()
