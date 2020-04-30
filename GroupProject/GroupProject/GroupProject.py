import requests
from bs4 import BeautifulSoup
import csv

href_element = []
animals_list = []

url = 'https://oceana.ca/en/marine-life/canadian-marine-life-encyclopedia'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'lxml')
section_element = retrieved_content.find('section', class_='block-callout-action-contain inner-contain flex-contain-wrap')

for h1_element in section_element.find_all('h1'):
    h1_text = h1_element.text
    animals_list.append(h1_text)

for article_element in section_element.find_all('article'):
    a_element = article_element.find('a')
    href_element.append('https://oceana.ca' + a_element['href'])


other_names = []
distribution = []
habitat = []
feeding_habits = []
conservation_status = []
taxonomy = []

# count = 0

for href in href_element:
    page_to_retrieve = requests.get(href)
    retrieved_content = BeautifulSoup(page_to_retrieve.content, 'lxml')
    # print(retrieved_content)
    div_element = retrieved_content.find('div', class_='animal-details-side animal-details-side-canada')
    # print(div_element)

    for p_element, h2_element in zip(div_element.find_all('p'), div_element.find_all('h2')):

        if h2_element.text == "Also known as":
            other_names.append(p_element.text.strip())
        if h2_element.text == 'Distribution':
            distribution.append(p_element.text.strip())
        if h2_element.text == 'Ecosystem/Habitat':
            habitat.append(p_element.text.strip())
        if h2_element.text == 'Feeding Habits':
            feeding_habits.append(p_element.text.strip())
        if h2_element.text == 'Conservation Status':
            conservation_status.append(p_element.text.strip())
        if h2_element.text == 'Taxonomy':
            taxonomy.append(p_element.text.strip())

other_names.insert(10, 'Nan')
other_names.insert(32, 'Nan')
other_names.insert(33, 'Nan')
other_names.insert(37, 'Nan')

conservation_status.insert(19, 'Threatened')

from itertools import zip_longest

dataToBeInserted = [animals_list, other_names, distribution, habitat, feeding_habits, conservation_status, taxonomy]
export_data = zip_longest(*dataToBeInserted, fillvalue = '')
with open('numbers.csv', 'w', encoding="utf-8", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Animal_Name", "Also_Known_As", "Distribution", "Habitat", "Feeding_Habits", "conservation_status", "Taxonomy"))
      wr.writerows(export_data)
myfile.close()

# LOAD CSV WITH HEADERS FROM 'file:///numbers.csv' AS Animals
# CREATE (:Animal { Animal_Name: Animals.Animal_Name, Also_Known_As: Animals.Also_Known_As,
# Distribution: Animals.Distribution,Habitat: Animals.Habitat, Feeding_Habits: Animals.Feeding_Habits,
# Conservation_Status: Animals.conservation_status, Taxonomy: Animals.Taxonomy })
#
# match (a:Animal),(b:Animal) where a.Habitat = b.Habitat and a<>b
# create (a)-[r:neighbour]->(b) return r

# match (a:Animal),(b:feeding_habits) where a.feeding_habit = b.feeding_habit
# create (a)-[r:Identical_Feeding_Habits]->(b) return r
#
# LOAD CSV WITH HEADERS FROM 'file:///feeding_habits.csv' AS Feeding_Habits
# CREATE (:Feeding_Habits { Feeding_Habits: Feeding_Habits.Feeding_Habits})
