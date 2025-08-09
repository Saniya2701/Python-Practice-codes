
products = [
    ("Pen", 10, True),          
    ("Notebook", 45, False),    
    ("Pencil", 5, True)      
]

for product in products:
    name = product[0]       
    price = product[1]    
    in_stock = product[2]  

    print("Product:", name)
    print("Price:", price)
    
    if in_stock == True:
        print("Status: In stock ")
    else:
        print("Status: Out of stock")
    
    print()  
