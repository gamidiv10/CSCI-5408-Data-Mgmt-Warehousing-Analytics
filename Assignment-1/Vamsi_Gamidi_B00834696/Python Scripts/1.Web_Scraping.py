import requests
from bs4 import BeautifulSoup

# Creation of lists to store the scraped data
grad_courses_tags = []
employee_list = []
grad_program_list = []
grad_program_tags = []
undergrad_program_list = []
undergrad_program_tags = []
macs_course_list = []
employee_office_nos = []
employee_office_nos_tags = []
employee_first_name = []
employee_last_name = []
employee_last_name_tags = []
employee_first_name_tags = []
employee_tag = []
advisers_list = []
adviser_first_name_list = []
adviser_last_name_list = []
advisers_first_name_tags = []
advisers_last_name_tags = []
advisers_tags = []
research_clusters = []
research_clusters_tags = []
faculties_list = []
faculty_dept_list = []
residence_list = []
library_list = []
archives_list = []
payment_methods = []
employee_dept_tags = []
dalplex_camps_list = []
climbing_programs_list = []
climbing_programs_tags = []


# Method to generate XML Tags
def generate_xml_tags(tag, value):
    return f"{tag}='{value}'"


# Method to insert generated xml data into xml file
def write_to_file(list, file):
    f = open(file, 'w+', encoding='utf-8')
    f.truncate()
    for i in list:
        f.write(f"\n{i}")
    return


# Method to write to all files
def write_to_files():
    write_to_file(advisers_tags, 'advisers.xml')
    write_to_file(grad_program_tags, 'grad_programs.xml')
    write_to_file(undergrad_program_tags, 'undergrad_programs.xml')
    write_to_file(grad_courses_tags, 'grad_courses.xml')
    write_to_file(employee_tag, 'faculty.xml')
    write_to_file(residences_tags, 'residences.xml')
    write_to_file(research_clusters_tags, 'research_clusters.xml')
    write_to_file(library_tags, 'libraries.xml')
    write_to_file(archives_tags, 'archives.xml')
    write_to_file(payment_methods_tags, 'payment_methods.xml')
    write_to_file(group_fitness_classes_tags, 'group_fitness_classes.xml')
    write_to_file(climbing_programs_tags, 'climbing_programs.xml')
    write_to_file(dalplex_camps_tags, 'dalplex_camps.xml')

    return


# graduate programsList - 1
grad_program_tags.append("<Programs>")
url = 'https://www.dal.ca/faculty/gradstudies/graduate-programs-admissions/programs.html'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
div_element = retrieved_content.find('div', class_='autoSearchContent dl-programsList')

for hyperlink_element in div_element.find_all('a'):
    hyperlink_text = hyperlink_element.get_text()
    try:
        grad_program_list.append(hyperlink_text.replace('&', 'and'))
        grad_program_tags.append("<Grad_Program " + generate_xml_tags('Program', hyperlink_text) + "/>")
    except AttributeError:
        continue
grad_program_tags.append("</Programs>")

# undergrad programsList - 2

undergrad_program_tags.append("<Undergrad_Programs>")
url = 'https://www.dal.ca/academics/programs.html'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
div_element = retrieved_content.find('div', class_='autoSearchContent dl-programsList')

for hyperlink_element in div_element.find_all('a'):
    hyperlink_text = hyperlink_element.get_text()
    url = 'https://www.dal.ca' + hyperlink_element['href']
    page_to_retrieve = requests.get(url)
    retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
    div_element = retrieved_content.find('div', class_='col-content')
    try:
        faculties_list.append(div_element.find('a').get_text())
    except AttributeError:
        continue
    try:
        undergrad_program_list.append(hyperlink_text)
    except AttributeError:
        continue

for i, j in zip(undergrad_program_list, faculties_list):
    undergrad_program_tags.append(
        "<Undergrad_Program " + generate_xml_tags('program', i.replace('&', 'and')) + " " + generate_xml_tags('Faculty',
                                                                                                              j.strip()) + "/>")
undergrad_program_tags.append("</Undergrad_Programs>")

# Grad Courses - 3
grad_courses_tags.append("<Macs_Courses>")
url = 'https://academiccalendar.dal.ca/Catalog/ViewCatalog.aspx?pageid=viewcatalog&catalogid=82&chapterid=4627&topicgroupid=19747&loaduseredits=False'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'lxml')
div_element = retrieved_content.find('div', class_='maincontent')
for ul_element in div_element.find_all('ul'):
    hyperlink_element = ul_element.find('a')
    try:
        macs_course_list.append(hyperlink_element.get_text())
        grad_courses_tags.append("<Course " + generate_xml_tags('Course', hyperlink_element.get_text()) + "/>")
    except AttributeError:
        continue
grad_courses_tags = list(dict.fromkeys(grad_courses_tags))
grad_courses_tags.append("</Macs_Courses>")

# advisers - 4
url = 'https://www.dal.ca/admissions/contactus/connect-with-an-advisor-.html'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
div_element = retrieved_content.find('div', class_='contentPar parsys')
for h4_element in div_element.find_all('h4'):
    h4_text = h4_element.get_text()
    try:
        advisers_list.append(h4_text)
    except AttributeError:
        continue
for i in advisers_list:
    i = i.rpartition(':')[0]
    j, k = i.split()
    adviser_first_name_list.append(j)
    adviser_last_name_list.append(k)

for i, j in zip(adviser_first_name_list, adviser_last_name_list):
    advisers_first_name_tags.append(generate_xml_tags('First_Name', i))
    advisers_last_name_tags.append(generate_xml_tags('Last_Name', j))

advisers_tags.append("<Stud_Advisers>")
for i, j in zip(advisers_first_name_tags, advisers_last_name_tags):
    advisers_tags.append("<Adviser " + i + " " + j + "/>")
advisers_tags.append("</Stud_Advisers>")

# faculty - 5
url = 'https://www.dal.ca/faculty/computerscience/faculty-staff.html'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
div_element = retrieved_content.find('div', class_='ctn-wrapper')
faculty = div_element.find('h2').find('a').get_text()
for table_element in div_element.find_all('table'):
    rows = table_element.find_all('tr')
    for row in rows:
        column = row.find_all('td')
        count = 0
        for col in column:
            count += 1
            if count == 1:

                try:
                    employee_list.append(col.get_text())
                    faculty_dept_list.append(faculty)
                except AttributeError:
                    continue
            if count == 3:
                try:
                    employee_office_nos.append(col.get_text())
                except AttributeError:
                    continue

# health sciences faculty
url = 'https://www.dal.ca/faculty/health/health-sciences/faculty-and-staff.html'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
div_element = retrieved_content.find('div', class_='contentPar parsys')
i = retrieved_content.find('div', class_='clearfix')
faculty = i.find('h2').find('a').get_text()
for li_element in div_element.find_all('li'):
    employee_list.append(li_element.get_text().split(',')[0])
    faculty_dept_list.append(faculty)
    employee_office_nos.append(" ")

for i in employee_list:
    i = i.lstrip('Dr.')
    try:

        j, k = i.split()
        employee_first_name.append(j)
        employee_last_name.append(k)
    except ValueError:
        continue

for i, j, k, l in zip(employee_first_name, employee_last_name, employee_office_nos, faculty_dept_list):
    employee_first_name_tags.append(generate_xml_tags('First_Name', i))
    employee_last_name_tags.append(generate_xml_tags('Last_Name', j))
    employee_office_nos_tags.append(generate_xml_tags('Office_No', k))
    employee_dept_tags.append(generate_xml_tags('Faculty', l))

employee_tag.append("<Employees>")
for i, j, k, l in zip(employee_first_name_tags, employee_last_name_tags, employee_office_nos_tags, employee_dept_tags):
    employee_tag.append("<faculty " + i + " " + j + " " + k + " " + l + "/>")

employee_tag.append("</Employees>")

# Residences - 6
residences_tags = ["<Residences>"]
url = 'https://www.dal.ca/campus_life/residence_housing/residence/halifax-campus/res-buildings-halifax.html'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
li_element = retrieved_content.find('li', class_='open')
for hyperlink_element in li_element.find_all('a'):
    residence_list.append(hyperlink_element.get_text())
    residences_tags.append("<Residence " + generate_xml_tags('Residence_Name', hyperlink_element.get_text()) + "/>")
residences_tags.append("</Residences>")



# Research Clusters - 7
research_clusters_tags.append("<Research_Clusters>")
url = 'https://www.dal.ca/research/SignatureResearchClusters.html'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
li_element = retrieved_content.find('li', class_='open')
ul_element = li_element.find('ul')
for hyperlink_element in ul_element.find_all('a'):
    research_clusters.append(hyperlink_element.get_text())
    research_clusters_tags.append(
        "<Research_Cluster " + generate_xml_tags('Cluster', hyperlink_element.get_text().strip()) + "/>")
research_clusters_tags.append("</Reseach_Clusters>")

# Libraries - 8
library_tags = ["<Libraries>"]
url = 'https://hours.library.dal.ca/'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'lxml')
div_element = retrieved_content.find('div', class_='span5 left-side')
for dt_element in div_element.find_all('dt')[1:]:
    library_list.append(dt_element.get_text().strip())
    library_tags.append(
        "<Library " + generate_xml_tags('Library_Name', dt_element.get_text().replace('&', 'and').strip()) + "/>")
library_tags.append("</Libraries>")

# Dal Archives recent submissions - 9
archives_tags = ["<Dal_Archives>"]
url = 'https://dalspace.library.dal.ca/handle/10222/16037'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'lxml')
div_element = retrieved_content.find('div', class_='ds-static-div secondary recent-submission')
for hyperlink_element in div_element.find_all('a')[:-1]:
    archives_list.append(hyperlink_element.get_text())
    archives_tags.append("<Archive " + generate_xml_tags('Archive_Submission', hyperlink_element.get_text()) + "/>")

archives_tags.append("</Dal_Archives>")
archives_tags = list(dict.fromkeys(archives_tags))
del archives_tags[1]


# Payment methods - 10
payment_methods_tags = ["<Payment_Methods>"]
url = 'https://www.dal.ca/admissions/money_matters/payment_due_dates.html'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
div_element = retrieved_content.find('div', class_='text parbase section')
for li_element in div_element.find_all('li')[3:]:
    payment_methods.append(li_element.get_text().strip())
    payment_methods_tags.append("<Payment_Method " + generate_xml_tags('payment', li_element.get_text().strip()) + "/>")
payment_methods_tags.append("</Payment_Methods>")

# Group fitness classes - 11
group_fitness_classes = []
group_fitness_classes_tags = ["<Group_Fitness_Classes>"]

url = 'https://athletics.dal.ca/programs-and-training/group-fitness-classes.html'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'html.parser')
div_element = retrieved_content.find('div', class_='contentPar parsys')
for b_element in div_element.find_all('b')[10:]:
    group_fitness_classes.append(b_element.get_text())
    group_fitness_classes_tags.append(
        "<Fitness_Class " + generate_xml_tags('Class', b_element.get_text().strip()) + "/>")
group_fitness_classes_tags.append("</Group_Fitness_Classes>")

# Climbing programs - 12
climbing_programs_tags.append("<Climbing_Programs>")
url = 'https://www.dalsports.dal.ca/Program/GetProducts?productTypeCV=00000000-0000-0000-0000-000000003502&classification=d436235a-4937-409e-98e5-09c1ec23dea5'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'lxml')
div_element = retrieved_content.find('div', class_='col-lg-9 col-md-9 col-sm-9 col-xs-12')
for h4_element in div_element.find_all('h4'):
    try:
        climbing_programs_list.append(h4_element.get_text())
        climbing_programs_tags.append(
            "<Climbing_Program " + generate_xml_tags('Program', h4_element.get_text().strip()) + "/>")
    except AttributeError:
        continue
climbing_programs_tags.append("</Climbing_Programs>")

# Dalplex Camps - 13
dalplex_camps_tags = ["<Dalplex_Camps>"]
url = 'https://www.dalsports.dal.ca/Program/GetProducts?classification=47af5f82-ac2a-4088-9c89-8e4b56089e7a'
page_to_retrieve = requests.get(url)
retrieved_content = BeautifulSoup(page_to_retrieve.content, 'lxml')
div_element = retrieved_content.find('div', class_='col-lg-9 col-md-9 col-sm-9 col-xs-12')
for h4_element in div_element.find_all('h4'):
    try:
        dalplex_camps_list.append(h4_element.get_text())
        dalplex_camps_tags.append("<Dalplex_Camp " + generate_xml_tags('Camp', h4_element.get_text()) + "/>")
    except AttributeError:
        continue
dalplex_camps_tags.append("</Dalplex_Camps>")

# Method call to write to all xml files
write_to_files()