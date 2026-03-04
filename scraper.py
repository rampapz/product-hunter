import requests
from bs4 import BeautifulSoup
import json
import random

URL = "https://www.amazon.in/gp/new-releases"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_amazon():

    products = []

    try:
        r = requests.get(URL, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        items = soup.select("img")

        for item in items[:20]:

            try:

                name = item.get("alt")

                image = item.get("src")

                if not name or not image:
                    continue

                trend = random.randint(80,95)
                price = random.randint(500,3000)

                products.append({
                    "name": name,
                    "category": "amazon",
                    "trend": trend,
                    "amazon": "https://amazon.in",
                    "image": image,
                    "amazon_price": price,
                    "supplier_price": int(price*0.4)
                })

            except:
                pass

    except:
        pass

    # fallback products if scraping fails
    if len(products) == 0:

        products = [

        {
        "name":"Portable Blender",
        "category":"fitness",
        "trend":94,
        "amazon":"https://amazon.in",
        "image":"https://m.media-amazon.com/images/I/61W3X0+2ZLL._AC_SL1500_.jpg",
        "amazon_price":999,
        "supplier_price":220
        },

        {
        "name":"Magnetic Phone Mount",
        "category":"gadgets",
        "trend":91,
        "amazon":"https://amazon.in",
        "image":"https://m.media-amazon.com/images/I/61g6k0Qk6UL._AC_SL1500_.jpg",
        "amazon_price":399,
        "supplier_price":90
        }

        ]

    return products


data = scrape_amazon()

with open("products.json","w") as f:
    json.dump(data,f,indent=2)
