# importing libraries
from bs4 import BeautifulSoup
import re
import pickle

# making soup for the whole page
pageSoup = BeautifulSoup(open('nit_agartala.html'), features='lxml')

# extracting only the peoples portion
people_card_class = 'grid grid__col--lg-8 block org-people-profile-card__profile-card-spacing'

# storing the extracted elements in a list
peoples = pageSoup.find_all('li', {'class': people_card_class})

# list to store all the peoples
alumnis = []

# extracting individual details of every people
i = 0
for people in peoples:
    i += 1
    if (i > 10):
        break
    # data to store
    name = ""
    profile_url = ""
    about = ""
    image = ""

    # a new soup for a people
    people_soup = BeautifulSoup(str(people), features='lxml')

    # element classes for name and about section
    people_name_class = 'ember-view lt-line-clamp lt-line-clamp--single-line org-people-profile-card__profile-title t-black'
    people_about_class = 'ember-view lt-line-clamp lt-line-clamp--multi-line'
    people_image_class = 'evi-image lazy-image ember-view'

    # finding name and about html portions and storing it as a string
    name_html_str = str(people_soup.find('div', {'class': people_name_class}))
    about_html_str = str(people_soup.find(
        'div', {'class': people_about_class}))
    people_image_str = str(people_soup.find(
        'div', {'class': people_image_class}))

    # regex pattern to remove the unnecessary html portion
    pattern = r'<div[^>]*>([^<]+)<!-- -->\s*</div>'

    # applying regex to name
    match = re.search(pattern, name_html_str)
    if match:
        extracted_name = match.group(1).strip()
        print(extracted_name)
        name = extracted_name
    else:
        print("Name not found in the HTML string.")

    # applying regex to about
    match = re.search(pattern, about_html_str)
    if match:
        extracted_about = match.group(1).strip()
        print(extracted_about)
        about = extracted_about
    else:
        print("About not found in html string")

    
    profile_url = people_soup.find('a').get('href')
    print(profile_url)

    # storing the data into a list of dictionaries
    alumnis.append({
        "name": name,
        "profile_url": profile_url,
        "about": about
    })


# checking the length of list
print(len(alumnis))


# stroing the data into binary format file to be used to feed database
with open('alumnis.json', 'wb') as f:
    pickle.dump(alumnis, f)
