a = 40
b = 5

#Arithmetic Operators
"""
print(f"a ; {a}")
print(f"b : {b }")

print(f"Addition : {a + b}")
print(f"substraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division:{a/b}")
print(f"Floor DivisionL: {a//b}")
print(f"Modulus: {a % b}")
print(f"Power: {a**b}")

"""
#Comparison Operators

price = 500
budget = 1000
'''
print(price < budget)
print(price > budget)
print(price == budget)
'''

#Assignment Operators
'''
value1 = 100
value2 = 100
value3 = 100

value1 += 20
print(value1)

value2 -= 22
print(value2)

value3 *= 2
print(value3)

'''


#profit report input 
product = input("Product: ")
sell_price = int(input("Selling Price: "))
cost_price = int(input("Cost Price: "))
quantity = int(input("Quantity: "))

#Calculating profit
profit_per_item = sell_price - cost_price
profit_total = (sell_price - cost_price) * quantity
profit_percentage = (profit_per_item / cost_price) * 100

print("========== ShopSphere Profit Report ==========")
print(f"Product: {product}")
print(f"Selling Price: {sell_price}")
print(f"Cost Price: {cost_price}")
print(f"Quantity: {quantity}")
print(f"Profit Per Item: {profit_per_item}")
print(f"Total Profit: {profit_total}")
print(f"Profit Percentage: {profit_percentage}%")
print("===============================================")



