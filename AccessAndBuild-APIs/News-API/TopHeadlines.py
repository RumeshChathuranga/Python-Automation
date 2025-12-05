import requests

# r = requests.get('https://newsapi.org/v2/everything?q=united%20states&from=2025-12-04&to=2025-12-04&sortBy=popularity&apiKey=31010a085bfb4a27b46d1fca39605834')


def get_news(country,api_key):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json() 
    articles = content['articles']

    results = []
    for article in articles:
        results.append(article['title'])
    return results

print(get_news('lk','31010a085bfb4a27b46d1fca39605834'))