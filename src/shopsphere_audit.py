
'''
#Dictionaries
customer1_details = {
    "c_id" : 4322,
    "c_name" : "Thahseen",
    "c_age" : "23",
    "c_location" : "Mooyikkal",
    "c_phone" : 7356336611,
    "c_total_spend" : 12202

}

print(customer1_details["c_phone"])
print(customer1_details["c_name"])

print(customer1_details.get("c_email", "Not Provided"))
customer1_details["c_total_spend"] += 200
print(customer1_details["c_total_spend"])

customer1_details["c_email"] = "thahseenjaf@gmail.com"
print(customer1_details["c_email"])


#tuples
tuple2 = (1202, 39832)
#tuple2[0] = 2
print(tuple2[0]) 


raw_datas = {101,11,344,101,11,21,21,1002}
set1 = set(raw_datas)
print(set1) #print without duplicates

blore_customer ={"C1","C2","C5","C4"}
vip_customer = {"C2", "C5"}

print(blore_customer & vip_customer)

'''

raw_categories = ["Electronics", "Fashion", "electronics", "Home", "FASHION", "Electronics", "Books"]
sorted1 = raw_categories.lower()
print(sorted1)