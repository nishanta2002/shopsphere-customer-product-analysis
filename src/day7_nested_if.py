cname = input("Customer Name :")
mtype = input("Membership type: ").capitalize()
amount = int(input("Purchase Amount: ₹"))

print(f"Customer : {cname}")
print(f"Membership : {mtype}")
print(f"Purchase Amount : ₹{amount}\n")

print("===== ShopSphere VIP Report =====")
if mtype == "Gold":
    if amount >= 5000:
            print("VIP Customer \nFree Delivery \nPremium Gift")
    else:
            print("Regular Gold Customer")
else:
    print("Standard Customer")

print("=================================")
