import requests

# r = requests.get('https://newsapi.org/v2/everything?q=united%20states&from=2025-12-04&to=2025-12-04&sortBy=popularity&apiKey=31010a085bfb4a27b46d1fca39605834')


def get_news(topic,from_date,to_date,api_key):
    url = f'https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={api_key}'
    r = requests.get(url)
    content = r.json() 
    articles = content['articles']

    results = []
    for article in articles:
        results.append(article['title'])
    return results

print(get_news('technology','2025-12-01','2025-12-04','31010a085bfb4a27b46d1fca39605834'))