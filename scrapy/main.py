from bs4 import BeautifulSoup
import requests
import simplejson as sj

search = input("input your search: ")
url = "https://www.daraz.pk/catalog/?"
params = {"q": search}

r = requests.get(url, params=params)
# print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
print(soup)


results = soup.find("div", {'class': 'c1_t2i'})


print(results)
