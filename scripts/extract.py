import requests
from dotenv import load_dotenv
import os

load_dotenv()

def extract_data(search_query="Phuket"):
    api_key = os.getenv("API_KEY")

    url = "https://api.content.tripadvisor.com/api/v1/location/search"

    params = {
        "key": api_key,
        "searchQuery": search_query,
        "language": "en"
    }

    headers = {
        "accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"{search_query}: {e}")
        return None

def run_queries():
    queries = [
        "temple in thailand",
        "cafe in thailand",
        "beach in thailand",
        "museum in thailand",
        "market in thailand",
        "park in thailand",
        "waterfall in thailand",
        "nightlife in thailand",
        "restaurant in thailand",
        "mountain in thailand",
        "island in thailand",
        "shopping mall in thailand",
        "spa in thailand",
        "zoo in thailand",
        "historic site in thailand"
    ]

    results = {}
    for q in queries:
        data = extract_data(q)
        results[q] = data
    return results

if __name__ == "__main__":
    all_data = run_queries()
    #print(all_data)
    print("All queries completed.")
