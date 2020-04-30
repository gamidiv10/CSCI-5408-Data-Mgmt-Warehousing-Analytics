import csv

# Lists to store words
positive_words_list = []
negative_words_list = []
bag_of_words = []

# Splitting positive, negative words and storing them as lists
def splitPositiveWords():
    with open("PositiveWords.txt", 'r') as PositiveWords:
        return PositiveWords.read().split("\n")

def splitNegativeWords():
    with open("NegativeWords.txt", 'r') as NegativeWords:
        return NegativeWords.read().split("\n")

positive_words_list = splitPositiveWords()
negative_words_list = splitNegativeWords()

# Writing polarity into files
with open("tweets.csv", 'r') as TweetsFile:
    with open('SentimentAnalysisOutput.csv', mode='w', newline='', encoding="utf-8") as OutputFile:
        csvWriter = csv.writer(OutputFile)
        csvWriter.writerow(['tweet', 'message', 'match', 'polarity'])
        TweetCount = 1
        for line in TweetsFile:
            bagDictionary = {}
            for word in line.split():
                if word in bagDictionary:
                    bagDictionary[word] = bagDictionary[word] + 1
                else:
                    bagDictionary[word] = 1
            bag_of_words.append(bagDictionary)

            IsAPostiveOrNegativeWord = False
            for matchedWord in bagDictionary.keys():
                if matchedWord in positive_words_list:
                    csvWriter.writerow([TweetCount, line.strip(), matchedWord, "Positive"])
                    IsAPostiveOrNegativeWord = True
                elif matchedWord in negative_words_list:
                    csvWriter.writerow([TweetCount, line.strip(), matchedWord, "Negative"])
                    IsAPostiveOrNegativeWord = True
            if not IsAPostiveOrNegativeWord:
                csvWriter.writerow([TweetCount, line.strip(), "", "Neutral"])

            TweetCount = TweetCount + 1
