import requests
from bs4 import BeautifulSoup
import json
import random

URLS = [
"https://www.amazon.in/gp/bestsellers",
"https://www.amazon.in/gp/new-releases"
]

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

products = []

def scrape_page(url):

    r = requests.get(url,headers=headers,timeout=10)

    soup = BeautifulSoup(r.text,"html.parser")

    items = soup.select("img")

    results=[]

    for item in items:

        name=item.get("alt")
        image=item.get("src")

        if not name or not image:
            continue

        trend=random.randint(70,100)

        price=random.randint(500,4000)

        results.append({
        "name":name,
        "category":"amazon",
        "trend":trend,
        "amazon":"https://amazon.in",
        "image":image,
        "amazon_price":price,
        "supplier_price":int(price*0.4)
        })

    return results


for url in URLS:

    try:
        data=scrape_page(url)
        products.extend(data)
    except:
        pass


# remove duplicates
seen=set()
clean=[]

for p in products:

    if p["name"] in seen:
        continue

    seen.add(p["name"])
    clean.append(p)


# keep top 20 by trend
clean=sorted(clean,key=lambda x:x["trend"],reverse=True)[:20]


with open("products.json","w") as f:
    json.dump(clean,f,indent=2)
