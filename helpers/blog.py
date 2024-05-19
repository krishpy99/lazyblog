import requests
from helpers.config import Settings
import json


env = Settings()
base_url = "https://api.medium.com/"
default_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', 
               "Upgrade-Insecure-Requests": "1",
               "DNT": "1",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

def get_author_id():
    path = "v1/me"
    headers = default_headers
    headers["Authorization"] = "Bearer " + env.medium_integration_key
    response = requests.get(base_url + path, headers=headers)
    res = json.loads((response.content).decode('utf-8'))
    return res

def write_blog(title, content, tags):
    author_id = get_author_id()["data"]["id"]

    path = "v1/users/" + author_id + "/posts"

    headers = default_headers
    headers["Authorization"] = "Bearer " + env.medium_integration_key
    headers["content-type"] = "application/json"

    payload = {
        "title": title,
        "contentFormat": "markdown",
        "content": content,
        "canonicalUrl": "",
        "tags": tags,
        "publishStatus": "public"
    }

    with open("text.json", "w") as t:
        json.dump(payload, t)

    response = requests.post(base_url + path, json=payload, headers=headers)
    res = json.loads((response.content).decode('utf-8'))
    print("article written.")
    return res