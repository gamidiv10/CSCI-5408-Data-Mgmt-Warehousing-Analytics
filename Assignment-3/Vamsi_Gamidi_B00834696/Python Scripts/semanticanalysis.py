import math
import csv
import requests
import json
import re
from newsapi.newsapi_client import NewsApiClient

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

AuthKey = {'Authorization': 'f134deec1d1f498c9e9f7a51c2bdbf19'}
urlForArticles = 'https://newsapi.org/v2/everything'
parametersForDalRetrieval = {'q': 'Dalhousie University', 'language': 'en',
                      'sortBy': 'relevancy', 'pageSize': 100}

parametersForHalifaxRetrieval = {'q': 'Halifax', 'language': 'en',
                      'sortBy': 'relevancy', 'pageSize': 100}

parametersForCanadaRetrieval = {'q': 'Canada', 'language': 'en',
                      'sortBy': 'relevancy', 'pageSize': 100}

parametersForUnivRetrieval = {'q': 'University', 'language': 'en',
                      'sortBy': 'relevancy', 'pageSize': 100}

parametersForEduRetrieval = {'q': 'Canada Education', 'language': 'en',
                      'sortBy': 'relevancy', 'pageSize': 100}

responseDal = requests.get(url=urlForArticles, headers=AuthKey, params=parametersForDalRetrieval)
responseHal = requests.get(url=urlForArticles, headers=AuthKey, params=parametersForHalifaxRetrieval)
responseCan = requests.get(url=urlForArticles, headers=AuthKey, params=parametersForCanadaRetrieval)
responseUniv = requests.get(url=urlForArticles, headers=AuthKey, params=parametersForUnivRetrieval)
responseEdu = requests.get(url=urlForArticles, headers=AuthKey, params=parametersForEduRetrieval)



response_json_string_dal = json.dumps(responseDal.json())
response_json_string_hal = json.dumps(responseHal.json())
response_json_string_can = json.dumps(responseCan.json())
response_json_string_univ = json.dumps(responseUniv.json())
response_json_string_edu = json.dumps(responseEdu.json())



response_dict_dal = json.loads(response_json_string_dal)
response_dict_hal = json.loads(response_json_string_hal)
response_dict_can = json.loads(response_json_string_can)
response_dict_univ = json.loads(response_json_string_univ)
response_dict_edu = json.loads(response_json_string_edu)

articles_list = response_dict_dal['articles'] + response_dict_hal['articles'] + response_dict_can['articles'] + response_dict_univ['articles'] + response_dict_edu['articles']

data = []

for article in articles_list:
    if article['author'] is None:
        article['author'] = 'Nan'
    if article['content'] is None:
        article['content'] = 'Nan'
    data.append({
        'Article_Title': remove_url(article['title']),
        'Article_Content': remove_url(article['content']),
        'Description': remove_url(article['description'])
    })
with open('articles_cleaned.json', 'w') as outfile:
    json.dump(data, outfile)
retrievedArticlesFile = "articles_cleaned.csv"
individualArticleFile = "article-"
fileCount = 1
wordsToFindFrequency = ['Canada', 'University', 'Dalhousie University', 'Halifax', 'Canada Education']


def createFilesForArticles(fileCount):
    with open(retrievedArticlesFile) as retrievedArticles:
        article = retrievedArticles.readline()
        while article:
            article = retrievedArticles.readline()
            articleFile = open(individualArticleFile + str(fileCount) + ".txt", "w")
            articleFile.write(article)
            articleFile.close
            fileCount += 1
    return fileCount

def findFrequency(wordstofindfrequency, fileCount):
    with open("TF-IDF.csv", mode='w', newline="", encoding="utf-8") as DocFreq:
        writer = csv.writer(DocFreq)
        # writer.writerow(['Total Documents', fileCount])
        # writer.writerow(
        #     ["Search Query", "Document containing term(df)",
        #      "Total Documents(N)/ number of documents term appeared(df)",
        #      "Log10(N/df)"])
        with open("FreqCount.csv", mode='w', newline="", encoding="utf-8") as FreqCountFile:
            max_relative_freq = -1

            writerFreqCount = csv.writer(FreqCountFile)
            # writerFreqCount.writerow(['Term', "Canada"])
            firstcolumn = "canada appeared in " + str(fileCount) + " documents"
            # writerFreqCount.writerow(
            #     [firstcolumn, "Total words (m)", "Frequency (f)", "Relative frequency (Rf)"])
            for word in wordstofindfrequency:
                i = 1
                j = 0
                while i < fileCount:
                    articleFile = open(individualArticleFile + str(i) + ".txt", "r")
                    filename = str(individualArticleFile + str(i) + ".txt")
                    article = articleFile.readline()
                    if article.find(word) != -1:
                        frequency = article.count(word)
                        totalWords = len(article.replace(","," ").split(" "))
                        frequency = frequency/totalWords
                        if word.lower() == "canada":

                            # writerFreqCount.writerow([str(filename), totalWords, frequency, str(frequency)])
                            j += 1
                    articleFile.close()
                    i += 1
                try:
                    df = totalFiles / j
                    log_df = math.log(df)
                    freq = str(fileCount) + "/"+ str(j)
                    # writer.writerow([word,str(j), str(freq), str(log_df)])
                except ZeroDivisionError:
                    continue

fileCount = createFilesForArticles(fileCount)

totalFiles = fileCount

findFrequency(wordsToFindFrequency, fileCount)

