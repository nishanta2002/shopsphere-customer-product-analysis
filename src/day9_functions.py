
'''
def welcome_customer(name):
    print(f"Welcome {name} to ShopShere!")

welcome_customer("bilal")
welcome_customer("thanu")
welcome_customer("rahul")'''

def calculate_bill(price, quantity):
    return price * quantity


bill1 = calculate_bill(599, 2)
bill2 = calculate_bill(200, 4)

print(bill1)
print(bill2)

print(f"TOTAL Revenue: {bill1 + bill2}")

def calc_gst(amount):
    return amount * 0.18

gst1 = calc_gst(bill1)
gst2 = calc_gst(bill2)

print(f" GST BILL 1 : {gst1}")
print(f" GST BILL 2 : {gst2}")


print(f" TOTAL BILL 1 : {gst1 + bill1:.2f}")
print(f" TOTAL BILL 2 : {gst2 + bill2}")

      