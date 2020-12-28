import requests

params = {'q': 'pizza'}
r = requests.get("http://www.google.com/search", params)
# print(r.text)
print(r.status_code)
print(r.headers)

f = open("./sample_page.html", "w+")
f.write(r.text)
f.close()
