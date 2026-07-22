count = int(input("How many customers today? : "))

for count in range(1, count + 1):
    print(f"===== Customer {count} ===== ")
    cname = input("Customer Name :")
    mtype = input("Membership type: ").capitalize()
    amount = int(input("Purchase Amount: ₹"))
    if mtype == "Gold":
        if amount >= 5000:
            print("Status : VIP Customer")
        else:
            print("Status : Regular Gold Customer")
    else:
        print("Status : Standard Customer")

print("=================================")