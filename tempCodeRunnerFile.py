#Explanation:GET request is sent to the URL using requests library.
#            .text attribute of the response object returns HTML content of the page as a string.

"""import requests
url = "https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/"
response = requests.get(url)
print(response.text)
print(response.status_code)"""

"""import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")

names = soup.find_all("a",class_ = "title")
product_list = []
for i in names:
    name = i.text.strip()
    product_list.append(name)
#print(product_list)

prices = soup.find_all("h4",class_ = "price float-end card-title pull-right")
prices_list = []
for i in prices:
    price = i.text.strip()
    prices_list.append(price)
#print(prices_list)

description = soup.find_all("p",class_="description card-text")
desc_list = []
for i in description:
    desc = i.text.strip()
    desc_list.append(desc)
#print(desc_list)


reviews = soup.find_all("p",class_="review-count float-end")
reviews_list = []
for i in reviews:
    revw = i.text.strip()
    reviews_list.append(revw)
#print(reviews_list)

df = pd.DataFrame({"Product_Name":product_list,"Prices":prices_list,"Description":desc_list,"Reviews":reviews_list})
print(df)

df.to_csv("Product_Details.csv")"""


import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")

#boxes = soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")
#print(boxes)
#print(len(boxes))

box = soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")[3]
#print(box)

name = box.find("a",class_="title")
print(name)

description=box.find("p",class_="description card-text").text
print(description)