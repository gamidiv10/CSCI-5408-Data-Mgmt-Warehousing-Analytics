import requests
import json
import re
from newsapi.newsapi_client import NewsApiClient

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

AuthKey = {'Authorization': 'f134deec1d1f498c9e9f7a51c2bdbf19'}
urlForArticles = 'https://newsapi.org/v2/everything'
parametersForRetrieval = {'q': '((Dalhousie University) OR (Halifax) OR (Canada) OR (University) OR (Canada Education))', 'language': 'en',
                      'sortBy': 'relevancy', 'pageSize': 100}

response = requests.get(url=urlForArticles, headers=AuthKey, params=parametersForRetrieval)
response_json_string = json.dumps(response.json())
response_dict = json.loads(response_json_string)
articles_list = response_dict['articles']

data = []

for article in articles_list:
    if article['author'] is None:
        article['author'] = 'Nan'
    if article['content'] is None:
        article['content'] = 'Nan'
    data.append({
        'Author': remove_url(article['author']),
        'Article_Title': remove_url(article['title']),
        'Article_Content': remove_url(article['content']),
        'Published_At': remove_url(article['publishedAt'])
    })
with open('articles_cleaned.json', 'w') as outfile:
    json.dump(data, outfile, default=myconverter)