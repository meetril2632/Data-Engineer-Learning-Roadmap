def my_func(z):
    if(z>10):
        print("Greater than 10 adding 1 to it")
        z+=1
    else:
        print("Returning the same value")
#Now if i return value in this function means it stores the value at the end of function call.
    return z

my_func(30)
returned_value = my_func(20)
print(returned_value)

# Can pass multiple parameters by defining def my_func(x,y,z):

# Pass so many values asterisk denotes that all passed values will be converted into tuple and passed as tuple
def my_func(*x):
    print(*x)
my_func(10,20,30,40)

# To pass as dictionary in the form of keys mapping use double asterisk
def my_func(**x):
    print(**x)
my_func(x=10,y=20,z=30,w=40)

# LAMBDA FUNCTION OPTIMIZING FUNCTIONS
# def add(x,y):
#     return x+y
# total=add(10,20)
# print(total)

add = lambda x,y : x+y