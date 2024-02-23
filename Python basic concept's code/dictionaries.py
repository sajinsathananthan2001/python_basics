customer = {
    "name": "Sajin Sathananthan",
    "age": 21,
    "is_verified": True
}


print(customer["name"])

#if you pass in get method if it not available it will pass "None"
print(customer.get("phone"))

#you can also pass default value
print(customer.get("phone","9597918475"))

#you can also update the datas
customer["name"] = "Sajin Jayanthi"

print(customer["name"])

