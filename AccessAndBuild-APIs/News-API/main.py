import requests

r = requests.get('https://newsapi.org/v2/everything?domains=wsj.com&apiKey=31010a085bfb4a27b46d1fca39605834')
content = r.json()
print(content['articles'][0]['title'])
print(content['articles'][0]['description'])