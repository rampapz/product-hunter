import json
import random

products = [

{
"name":"Portable Blender",
"category":"fitness",
"trend":random.randint(80,95),
"amazon":"https://amazon.in",
"image":"https://m.media-amazon.com/images/I/61W3X0+2ZLL._AC_SL1500_.jpg",
"amazon_price":999,
"supplier_price":220
},

{
"name":"Magnetic Phone Mount",
"category":"gadgets",
"trend":random.randint(80,95),
"amazon":"https://amazon.in",
"image":"https://m.media-amazon.com/images/I/61g6k0Qk6UL._AC_SL1500_.jpg",
"amazon_price":399,
"supplier_price":90
}

]

with open("products.json","w") as f:

json.dump(products,f,indent=2)
