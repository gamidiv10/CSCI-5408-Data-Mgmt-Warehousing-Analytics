inFile = open(
    'C:\\Users\\vamsi\\Materials\\Data Mgmt, Warehousing, Analytics\\CaseStudy\\14100224-eng\\FileToBeCleaned.csv',
    'r', encoding="utf8")
outFile = open(
    'C:\\Users\\vamsi\\Materials\\Data Mgmt, Warehousing, Analytics\\CaseStudy\\14100224-eng\\FileToBeImported.csv',
    'w+', encoding="utf8")
listLines = []
for line in inFile:
    if line in listLines:
        continue
    else:
        outFile.write(line)
        listLines.append(line)
outFile.close()
inFile.close()
