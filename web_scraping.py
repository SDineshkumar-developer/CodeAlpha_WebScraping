import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article")

data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    data.append([title, price])

df = pd.DataFrame(data, columns=["Title", "Price"])

df.to_csv("books.csv", index=False)

print(df.head())
print("Data saved successfully!")
