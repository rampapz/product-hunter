import requests
from bs4 import BeautifulSoup
import json
import random

URL = "https://www.amazon.in/gp/new-releases"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_amazon():

    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    products = []

    items = soup.select(".zg-grid-general-faceout")

    for item in items[:20]:

        try:

            name = item.select_one("img")["alt"]
            image = item.select_one("img")["src"]

            link = item.select_one("a")["href"]
            link = "https://amazon.in" + link

            trend = random.randint(80,95)

            price = random.randint(300,5000)
            supplier = int(price * 0.4)

            products.append({
                "name": name,
                "category": "amazon",
                "trend": trend,
                "amazon": link,
                "image": image,
                "amazon_price": price,
                "supplier_price": supplier
            })

        except:
            pass

    return products


data = scrape_amazon()

with open("products.json","w") as f:
    json.dump(data,f,indent=2)
