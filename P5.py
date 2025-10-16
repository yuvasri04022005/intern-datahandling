import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = "http://quotes.toscrape.com"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# Step 2: Extract quotes and authors
quotes = []
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    quotes.append({"Quote": text, "Author": author})

# Step 3: Convert to DataFrame
df_quotes = pd.DataFrame(quotes)
print(df_quotes.head())
