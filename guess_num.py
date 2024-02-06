list_of_items = [34, 23, 43, 23]
list_of_items2 = [item ** 2 for item in list_of_items]
list_of_items2.append("Rajendra")
print(list_of_items2)
list_of_items2[2] = "Monument"
print(list_of_items2)
print(type("monument"))
print(type(True))

print(type(list_of_items2[3]))

dictionary_key_value = {
    "name": "Rajendra Niroula",
    "age": 24,
    "address": "Bhaktapur"
}

dictionary_key_value.update({"occupation": "Unemployed"})
print(dictionary_key_value)