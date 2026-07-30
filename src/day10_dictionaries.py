customer_details = []

details_count = int(input("Enter the number of details you need to add : "))

for n in range(1, details_count+1):

    cusomter= {}
    print(f"\n Customers No :{n}")

    cusomter["name"] = input("Enter name: ")
    cusomter["Membership"] = input("Enter membership : ")
    cusomter["Age"] = input("Enter age: ")
    cusomter["Total Amount"] = int(input("Enter Amount Total: "))
    customer_details.append(cusomter)

print("\n ====== BILL ====== ")

for cusomter in customer_details:

    print("-----------------------------")

    
    for key in cusomter:
            print(f"{key}: {cusomter[key]}")

print(customer_details)
print(cusomter)