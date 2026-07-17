# membership discount system

#custome details
cname = input("Enter Your Name:")
amount = int(input("Enter the purchased amount: ₹"))
membtype = input("Select your Membership Type : (Gold / Silver / Regular)").capitalize()


#output
print("="*10," ShopSphere Discount ", "="*10)
print(f"Customer : {cname}")
print(f"Membership : {membtype}")
print(f"Purchase Amount : ₹{amount}")



#if else 
if membtype == "Gold":
    final_amount = amount - ((amount * 10)/100)
    discount = (amount * 10)/100
    print(f"Discount : 10% (₹{discount:.2f})")
    print(f"Final Amount : ₹{final_amount:.2f}")

elif membtype == "Silver":
   final_amount = amount - ((amount * 5)/100)
   discount = (amount * 5)/100
   print(f"Discount : 5% (₹{discount:.2f})")
   print(f"Final Amount : ₹{final_amount:.2f}")

elif membtype == "Regular":
    discount = 0
    final_amount = amount
    print(f"Discount : ₹{discount:.2f}")
    print(f"Final Amount : ₹{final_amount:.2f}")


else:
    print("Invalid Input")

print("Thank you")
print("=" * 42)

    



