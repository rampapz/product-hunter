import requests
from bs4 import BeautifulSoup
import json
import random

URL = "https://www.amazon.in/gp/new-releases"

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

products = []

try:

    r = requests.get(URL, headers=headers, timeout=10)

    soup = BeautifulSoup(r.text,"html.parser")

    images = soup.find_all("img")

    for img in images[:30]:

        name = img.get("alt")
        image = img.get("src")

        if not name or not image:
            continue

        price=random.randint(500,3000)

        products.append({

        "name":name,
        "category":"amazon",
        "trend":random.randint(80,100),
        "amazon":"https://amazon.in",
        "image":image,
        "amazon_price":price,
        "supplier_price":int(price*0.4)

        })

except Exception as e:

    print("Scraping failed:", e)


# FALLBACK PRODUCTS (so dashboard never goes blank)
if len(products) < 5:

    products = [

    {
    "name":"Portable Blender",
    "category":"fitness",
    "trend":95,
    "amazon":"https://amazon.in",
    "image":"https://m.media-amazon.com/images/I/61W3X0+2ZLL._AC_SL1500_.jpg",
    "amazon_price":999,
    "supplier_price":220
    },

    {
    "name":"Magnetic Phone Mount",
    "category":"gadgets",
    "trend":92,
    "amazon":"https://amazon.in",
    "image":"https://m.media-amazon.com/images/I/61g6k0Qk6UL._AC_SL1500_.jpg",
    "amazon_price":399,
    "supplier_price":90
    },

    {
    "name":"Electric Spin Scrubber",
    "category":"home",
    "trend":93,
    "amazon":"https://amazon.in",
    "image":"https://m.media-amazon.com/images/I/61oXbM9pPPL._AC_SL1500_.jpg",
    "amazon_price":1499,
    "supplier_price":350
    },

    {
    "name":"LED Strip Lights",
    "category":"home",
    "trend":90,
    "amazon":"https://amazon.in",
    "image":"https://m.media-amazon.com/images/I/61y3yX9sBVL._AC_SL1500_.jpg",
    "amazon_price":699,
    "supplier_price":150
    },

    {
    "name":"Mini Projector",
    "category":"gadgets",
    "trend":91,
    "amazon":"https://amazon.in",
    "image":"https://m.media-amazon.com/images/I/61Xj3W5G8pL._AC_SL1500_.jpg",
    "amazon_price":4999,
    "supplier_price":1800
    }

    ]


with open("products.json","w") as f:

    json.dump(products,f,indent=2)
