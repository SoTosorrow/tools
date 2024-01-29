
import requests

from config import google_config as config


# custom
proxy = { "http": "http://127.0.0.1:7897", "https": "http://127.0.0.1:7897"}
google_search_endpoint = "https://www.googleapis.com/customsearch/v1"
query_num = 8

def invokeGoogleSearch(query):
    params = {
        "key": config["key"],
        "cx": config["search_engine_id"],
        "q": query,    # search content
        "num": query_num,
    }
    res = requests.get(
        google_search_endpoint,
        params=params,
        proxies=proxy
    )
    """
        kind, title, htmlTitle, link, displayLink, snippet....
    """
    json_content = res.json()
    contexts = json_content["items"][:query_num]

    results = [
            {
                'kind':i['kind'], 
                'title':i['title'],
                'link':i['link']
            } for i in contexts]
    return results

if __name__ == '__main__':
    query = "rust dyn trait fat pointer"
    r = invokeGoogleSearch(query)
    print(r)