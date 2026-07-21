product = int(input("How many products do you want to enter?"))

for i in range(1,product +1):
    pname = input("Product Name:")
    price = int(input("Price:"))
    quantity = int(input("Quantity: "))
    print(f"Product Name: {pname}")
    print(f"Price: ₹{price}")
    print(f"Quantity: {quantity}")
    print(f"Total: ₹{price*quantity}")