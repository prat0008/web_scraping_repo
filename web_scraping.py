#project - tata ipl auction stats 

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

# Find the specific table first
table = soup.find("table", class_="ih-td-tab w-100 auction-tbl")

# Then find headers ONLY within that table
if table:
    headers = table.find_all("th")
    title_list = [header.text.strip() for header in headers]
    #print(title_list)
else:
    pass
    #print("Table not found")

df=pd.DataFrame(columns=title_list)

points_data=table.find_all("tr")
for i in points_data[1:]:
    data=i.find_all("td")
    points_data=[tr.text.strip() for tr in data]
    l=len(df)
    df.loc[l]=points_data
print(df)
df.to_csv("Tata_IPL-Auction_Stats.csv")