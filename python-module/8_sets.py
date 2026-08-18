# Set also eliminates the duplicate values also
my_set = {1,2,3,4,5}
my_set2 = {1,2,3,4,5,5,5,5,5,5}
b = {10,22,2,3,4}
print(my_set2) # -> prints 1,2,3,4,5 only

print(my_set2.union(b)) # Union means only those elements which are not present in "my_set" and non-repetitive
print(my_set2.intersection(b)) # Intersection means only common elements of both sets (by default they are non-rep as  set itself is non-rep)

my_set2.remove(2)
my_set2.add(20) # Adds at end
print(my_set2)

# If set and dictionaries denotion then how to create an empty for those
a = {} # This is empty "dict"
b = set() # This is empty set, you can check using print(type(a)) or print(type(b))