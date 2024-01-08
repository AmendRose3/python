#key value pairs
#each key is unique
customer={
    "name":"john",
    "age":56,
}
print(customer.get("name"))
#if the key dosent exist it returns none else we can give a default value
print(customer.get("willingness","no"))
#we add a key value pair like:
customer["willingness"]="yes"
print(customer)