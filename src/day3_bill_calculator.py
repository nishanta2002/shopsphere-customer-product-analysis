#basic input details
customer_name = input("Enter your name: ")
product_name = input("Enter product name: ")
price=int(input("enter the price:"))
quantity=int(input("Quantity :"))
discount=int(input("enter the discount %:"))

#bill Generation Part
print ("\n```````````````ShopShere BILL``````````````")
print("Customer Name: ",customer_name)
print("Product Name: ",product_name)
print("Price of the product: ",price)
print("Quantity: ",quantity)


total_price=price*quantity
print("Total Price: ",total_price)

#dicount calculation
discount_price=total_price-((total_price * discount)/100)
print("total price after discount: ",(discount_price))
print(type(price))

print ("\n```````````````Thank you for shopping with us```````````````")
