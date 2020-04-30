source_file = open(
    'C:\\Users\\vamsi\\Materials\\Data Mgmt, Warehousing, Analytics\\google-play-store-apps\\googleplaystore_user_reviews.csv',
    'r', encoding="utf8")
destination_file = open(
    'C:\\Users\\vamsi\\Materials\\Data Mgmt, Warehousing, Analytics\\google-play-store-apps\\googleplaystore_user_reviews_2.csv',
    'w+', encoding="utf8")
lines_list = []
for line in source_file:
    if line in lines_list or line.__contains__('nan'):
        continue
    else:
        destination_file.write(line)
        lines_list.append(line)
destination_file.close()
source_file.close()
