fileForTweets= open("tweets.txt","r")
finalCountFileForTweets = open("tweets2.txt", "w+")

for line in fileForTweets.readlines():
    if line.lower().startswith('canada:') or line.lower().startswith('education:') or line.lower().startswith('university:') or line.lower().startswith('dalhousie:') or line.lower().startswith('expensive:') or line.lower().startswith('good school:') or line.lower().startswith('good schools:') or line.lower().startswith('bad school:') or line.lower().startswith('bad schools:') or line.lower().startswith('poor school:') or line.lower().startswith('poor schools:') or line.lower().startswith('faculty:') or line.lower().startswith('computer science:') or line.lower().startswith('graduate:'):
        finalCountFileForTweets.write(line + '\n')


fileForArticles = open("articles.txt", "r")
finalCountFileForArticles = open("articlesWordCount.txt", "w+")
for line in fileForArticles.readlines():
    if line.lower().startswith('canada:') or line.lower().startswith('education:') or line.lower().startswith('university:') or line.lower().startswith('dalhousie:') or line.lower().startswith('expensive:') or line.lower().startswith('good school:') or line.lower().startswith('good schools:') or line.lower().startswith('bad school:') or line.lower().startswith('bad schools:') or line.lower().startswith('poor school:') or line.lower().startswith('poor schools:') or line.lower().startswith('faculty:') or line.lower().startswith('computer science:') or line.lower().startswith('graduate:'):
        finalCountFileForArticles.write(line + '\n')
