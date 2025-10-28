mason_store = [ 

{ 

    "itemnumber": "0", 
    "name": "RTX 5090",
    "price": 4000,
    "rating": "High End",
    "description": "32 GB of GDDR7 Memory and currently the latest of Nvidias 50 series graphics cards.",
    "amount": 0
    
},


 
 {   
    "itemnumber": "1",
    "name": "Apple Airpods Max",
    "price": 500, 
    "rating": "Mid End",
    "description": "Headphones with great noise cancellation features and compatible with all of Apples Products.",
    "amount": 0

},
{   
    "itemnumber": "2",
    "name": "Iphone 17 pro",
    "price": 1000,
    "rating": "High end",
    "description": "Apple's latest Iphone with the newest Apple 19 chip and a 48 megapixel camera",
    "amount": 0
},
{   
    "itemnumber": "3",
    "name": "Xiyang phone",
    "price": 1000000,
    "rating": "High End",
    "description": "A phone made of 24 karat gold with Xiyangs face on it",
    "amount": 0
},
{   
    "itemnumber": "4",
    "name": "Mr. Whalen Key Board",
    "price": 1,
    "rating": "Low End",
    "description": "A keyboard with MR. Whalen's face on every key cap. Once every 100 presses this keyboard will lower your HOS.",
    "amount": 0
}

]
 
total = 0

cart = ""


for index, item in enumerate(mason_store):
    print(index, ':',item['itemnumber'], item['name'], item['price'], item ['description'], item['rating'])
    

while cart != "done" :
    cart = input("Input what you want. type 'done' when done")
    
    for item in mason_store:
        if cart == item["itemnumber"]:
            item["amount"] = item["amount"] + 1
            

for item in mason_store:
    if item['amount'] > 0:
        total = (item['amount'] * item['price']) + total 

if cart == "done":
    for item in mason_store:
        if item['amount'] > 0:
            print(f" You have {item['name']} {item['amount']}")
            
print(f" Your total is {total}")