from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

username = driver.find_element(By.ID, "username")

username.send_keys("<Linkedin email>")

pword = driver.find_element(By.ID, "password")

pword.send_keys("<Linkedin Password>")


driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

profile_url = "https://www.linkedin.com/in/aditya-ajay2662?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAADLSeU0BZ1fo6vNPtOq9-dv1gXRfKFzaTrg"
driver.get(profile_url)

start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    initialScroll = finalScroll
    finalScroll += 1000
    time.sleep(3)
    end = time.time()
    if round(end - start) > 20:
        break

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
print(intro)
name_loc = intro.find("h1")
name = name_loc.get_text().strip()
works_at_loc = intro.find("div", {'class': 'text-body-medium'})
works_at = works_at_loc.get_text().strip()


location_loc = intro.find_all("span", {'class': 'text-body-small'})
location = location_loc[0].get_text().strip()

print("Name -->", name, "\nWorks At -->", works_at, "\nLocation -->", location)
