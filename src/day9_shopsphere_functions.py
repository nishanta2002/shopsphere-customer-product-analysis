def calculate_bill(price, quantity):
    return price * quantity

def calculate_discount(total):
        if total >= 5000:
            return total * 0.10
        else:
            return 0

def final_price(total, discount):
      return total - discount

print("----- ShopShere Bill Entry------ ")
price = int(input("Enter the Price : "))
quantity = int(input("Enter the Quantity : "))

total = calculate_bill(price, quantity)
discount = calculate_discount(total)
final = final_price(total, discount)

print("----- ShopShere Bill Generated Successfully ------ ")
print(f"Total price : {total:.2f}")
print(f"Total Discount : {discount:.2f}")
print(f"Final Amount : {final:.2f}\n")

print("-----         THANK YOU         ------ ")
 

         
