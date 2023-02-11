import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}



URL = "https://quizlet.com/32444309/introduction-to-computer-science-flash-cards/"
page = requests.get(URL)
#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.select('a.SetPageTerm-wordText')


#results = soup.find(id="challenge-body-text")
print(results)

#ob_elements = results.find_all("div", class_="SetPageTarget")