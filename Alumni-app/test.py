from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

import re
import pickle

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

username = driver.find_element(By.ID, "username")

username.send_keys("<Linked Username")

pword = driver.find_element(By.ID, "password")

pword.send_keys("<Password>")


driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

alumni_url = "https://www.linkedin.com/school/national-institute-of-technology-agartala/people/"
driver.get(alumni_url)

start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
    driver.execute_script(
        f"window.scrollTo({initialScroll},{initialScroll - 200})")
    driver.execute_script(
        f"window.scrollTo({initialScroll - 200},{initialScroll})")
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    initialScroll = finalScroll
    finalScroll += 1000
    time.sleep(1)
    end = time.time()
    if round(end - start) > 20:
        break

# making soup for the whole page
src = driver.page_source
pageSoup = BeautifulSoup(src, 'lxml')

# extracting only the peoples portion
people_card_class = 'grid grid__col--lg-8 block org-people-profile-card__profile-card-spacing'

# storing the extracted elements in a list
peoples = pageSoup.find_all('li', {'class': people_card_class})

print("No. of peoples scrolled through = ", len(peoples), "In 20 seconds")

# list to store all the peoples
alumnis = []

# extracting individual details of every people
for people in peoples:
    name = ""
    profile_url = ""
    about = ""
    image_url = ""

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
        name = extracted_name

    # applying regex to about
    match = re.search(pattern, about_html_str)
    if match:
        extracted_about = match.group(1).strip()
        about = extracted_about

    pu = people_soup.find('a')
    if pu:
        profile_url = people_soup.find('a').get('href')

    iu = people_soup.find('img', {'class': people_image_class})
    if iu:
        image_url = people_soup.find(
            'img', {'class': people_image_class}).get('src')

    alumnis.append({
        "name": name,
        "profile_url": profile_url,
        "about": about,
        "image_url": image_url
    })

print(len(alumnis))
print(alumnis[0])

with open('alumnis.json', 'wb') as f:
    pickle.dump(alumnis, f)
