mason_store = [ 

{ 
    "name": "RTX 5090",
    "price": 4000,
    "rating": "High End",
    "description": "32 GB of GDDR7 Memory and currently the latest of Nvidias 50 series graphics cards."

},


 
   { "name": "Apple Airpods Max",
    "price": 500, 
    "rating": "Mid End",
    "description": "Headphones with great noise cancellation features and compatible with all of Apples Products."
},
{  
    "name": "Iphone 17 pro",
    "price": 1000,
    "rating": "High end",
    "description": "Apple's latest Iphone with the newest Apple 19 chip and a 48 megapixel camera"

},
{
    "name": "Xiyang phone",
    "price": 1000000,
    "rating": "High End",
    "description": "A phone made of 24 karat gold with Xiyangs face on it"
},
{
    "name": "Mr. Whalen Key Board",
    "price": 1,
    "rating": "Low End",
    "description": "A keyboard with MR. Whalen's face on every key cap. Once every 100 presses th keyboard will talk about the world's issues."
}

]

for index, item in enumerate(mason_store):
    print(index, ':', item['name'])

cart = input("Input your cart like this: 0, 1, 2, 3, 4 You CAN repeat numbers.")
rtx = 0
max = 0
phone = 0
xiyang = 0
whalen = 0
total = 0
for char in cart:
    if char == "0":
        rtx = rtx + 1
        total += + 4000
    elif char == "1":
        max = max + 1
        total += 500
    elif char == "2":
        phone = phone + 1
        total += 1000
    elif char == "3":
        xiyang = xiyang + 1
        total += 1000000
    elif char == "4":
        whalen = whalen +1
        total += 1