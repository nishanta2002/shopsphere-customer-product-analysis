
'''
products = []

products.append("Mobile")
products.append("Headphones")
products.append("Laptop")
products.append("Books")

print(products)
print(len(products))

products.remove("Books")
print(products)

'''

count = int(input("How many products?"))
list1 = []
for n in range(1,count + 1):
    list1.append(input(f"Product {n} : "))
    
print("===== Inventory =====")    
for products in list1:
        print(products)
print(f"\nTotal Products : {count}")
