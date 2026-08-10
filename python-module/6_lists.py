my_list = [1,2,"Meet","Poshia",['aa','bb','cc']]

#Index printing in list
print(my_list[4][1])

#Slicing
print(my_list[0:3])
print(my_list[-3:]) # Last three elements of the list in ascending declared format only, here empty means length of my_list
#If you want to use - then, in indexing -1 is the last element, -2 is second last element
#What is does under the hood is
print(my_list[(len(my_list)-3):(len(my_list))])
print(my_list[-1:])
#Gap skipping/jump
print(my_list[0::2])

my_list.append("Hero") #lista are mutable and append only at last
print(my_list)

my_list.insert(1,"Hero") #lista are mutable and insert anywhere in list
my_list.pop() #Removes last element
my_list.remove("Meet")
print(my_list)

#Reverse a list
for i in reversed(my_list):
    print(i)

#or
print(my_list[::-1])

my_list = [1,2,3,4,5,6]
print(my_list[-5:-2])

# COMPREHENSIVE LISTS
my_list = [1,2,3,4,5,6]

# We want our list modified into i*i for each element instead of writing a loop code replacing i to i*i
# Should write output in the list then for loop then conditions if required/multiple conditions as well permissible
new_list = [i*i for i in my_list]

print(new_list)

#Check even using comprehensive lists
new_list = [i for i in my_list if (i%2) == 0 if (i!=6)]
print(new_list)