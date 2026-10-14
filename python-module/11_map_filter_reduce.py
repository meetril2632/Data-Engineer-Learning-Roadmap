# Function accepting list
my_list = [1,2,3,4,5]

def square(x):
    returned_list = [i*i for i in x]
    print(returned_list)

square(my_list)

# -------------------------------------------

# Now this is a long workaround, but a direct function to pass each item of list and full list as well using MAP
my_list = [1,2,3,4,5]

def square(x):
    return x*x

result = list(map(square, my_list)) # map(<function>, <iterable data>) square function applied to passed list whose output is
# list so need to store and print in list format only
print(result)

# --------------------------------------------

# Now if i add condition to apply to the number who are only even in function itslef map will return "None" to number
# which did not passed the condition so to remove those "None" ones from output list we use "FILTER" function
my_list = [1,2,3,4,5]

def square(x):
    if(x % 2 == 0):
        return x*x

result = list(filter(square, my_list))
print(result)

# --------------------------------------------

# Now to use reduce you need to import "REDUCE" first
# It takes first two values from passed list and applies the function and reduces the list for final output
# So what happens 1+2=3, then 3+3=6, then 6+4=10, then 10+5=15, 15 is the output
from functools import reduce

my_list = [1,2,3,4,5]

def square(x,y):
        return x+y
result = reduce(square, my_list)
print(result)