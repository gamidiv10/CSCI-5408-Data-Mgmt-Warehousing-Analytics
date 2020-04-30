import pymongo
from pymongo import MongoClient
from bson.code import Code

mongoDBConnection = MongoClient('localhost:27017')
databaseForTweetsArticles = mongoDBConnection.mydb

mapForTweetsMultipleWords = Code(open('wordMapForMultipleWords.js', 'r').read())
mapForTweetsSingleWords = Code(open('wordMapForSingleWords.js', 'r').read())
reduce = Code(open('wordReduce.js', 'r').read())
mapForArticlesSingleWords = Code(open('wordMapForArticles.js', 'r').read())
mapForArticlesMultipleWords = Code(open('wordMapForArticlesMultipleWords.js', 'r').read())


fileForSearchInTweets = open("tweets.txt","w+")
resultsMultipleWords = databaseForTweetsArticles.tweets.map_reduce(mapForTweetsMultipleWords, reduce, "resultsMultipleWords")
for result in resultsMultipleWords.find():
    fileForSearchInTweets.write(result['_id'] + ':' + '%d'%result['value']['count'] + '\n')



singleWordResults = databaseForTweetsArticles.tweets.map_reduce(mapForTweetsSingleWords, reduce, "singleWordResults")
for result in singleWordResults.find():
    fileForSearchInTweets.write(result['_id'] + ':' + '%d'%result['value']['count'] + '\n')

fileForSearchInArticles = open("articles.txt", "w+")
resultsMultipleWords = databaseForTweetsArticles.Articles.map_reduce(mapForArticlesMultipleWords, reduce, "resultsMultipleWords")
for result in resultsMultipleWords.find():
    fileForSearchInArticles.write(result['_id'] + ':' + '%d'%result['value']['count'] + '\n')

singleWordResults = databaseForTweetsArticles.Articles.map_reduce(mapForArticlesSingleWords, reduce, "singleWordResults")
for result in results.find():
    fileForSearchInArticles.write(result['_id'] + ':' + '%d'%result['value']['count'] + '\n')