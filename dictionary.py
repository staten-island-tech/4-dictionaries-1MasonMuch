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
    "description": "A keyboard with MR. Whalen's face on every key cap. Once every 100 presses this keyboard will lower your HOS."
}

]

rtx = 0
max = 0
phone = 0
xiyang = 0 
whalen = 0
total = 0 
cart = ""


for index, item in enumerate(mason_store):
    print(index, ':', item['name'], item['price'], item ['description'], item['rating'])
    
    
while cart != "done" :
    cart = input("Input what you want. type 'done' when done")
    for i in mason_store:
        if cart.lower() == mason_store.lower():


print(f"You have orderd {rtx} RTX 5090(s), {max} Apple Airpods Max(s), {phone} Iphone 17 pro(s), {xiyang} Xiyang phone(s), and {whalen} Mr. Whalen Key Board(s)")
print("__________________________________________________________________________________________________________________________________________________________________")
print(f"your cart total is {total} dollas.")