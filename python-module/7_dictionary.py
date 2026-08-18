# "Key":Value
my_dict = {"x":1, "y":2, "z":3}
print(my_dict)

my_dict["x"] = 10

my_dict.pop("z")

print(my_dict.keys()) # Prints only keys from dictionary
print(my_dict.values()) # Prints only values of keys from dictionary
print(my_dict.items()) # Prints keys with their corresponding values from dictionary

# Inhertied dictionaries
my_dict = {"x":1, "y":2, "z":3, "demo":{"a":1, "b":2, "c":3}}
print(my_dict)
print(my_dict.items()) 
print(my_dict["demo"]["b"])