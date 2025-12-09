import requests
import json

url = 'https://api.languagetool.org/v2/check'
data = {
    'text': 'this is a sple test for testing with errs',
    'language': 'auto',
    
}

response = requests.post(url, data=data)
results = json.loads(response.text)
for match in results['matches']:
    print(f"Error: {match['message']}")
    print(f"Context: {match['context']['text']}")
    print(f"Suggested Replacements: {[rep['value'] for rep in match['replacements']]}")
