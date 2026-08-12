# String in python behaves same as array of characters, acts as an array
# y = ['M', 'E', 'E', 'T']
x = "MeetPoshia"
print(x[1])

# Slicing string
# Print first four characters of x string x[0:n-1]
print(x[0:4]) # -> Here upper value is not included.
print(x[3:7])

print(x[:]) # If nothing before the colon then by default it takes 0 and after colon n as the end-point (len(string))
print(x[0:len(x)])

# upper lower functions - converts all characters into upper lower cases
print(x.upper())

# replace fuction
print(x.replace("M","B"))

# split function - automatically splits your string based on character and store all items within a list
x = "Meet Poshia Love"
my_list = x.split(" ") # -> Space " " is also a separator
print(my_list)

# startswith and endswith functions
# SCENARIO 1 - If you want to only read file which are just .csv files 
fileName = "raw_data.csv"

if(fileName.endswith(".csv")):
    print("CSV File")

# Count function
statement = "I am Meet Poshia. Meet Poshia is my name. Meet loves football. Meet is a blaugrana supporter."
print(statement.count("Meet"))

# isnumeric(), isalnum() - alphaNumeric
demo_str = "Meet" # False
demo_var = 10 # Error - Because this function only works on string
demo_num = "10" # True - mumber encapsulated in double inverted comma is passed.
demo_alnum = "10abc" # True
print(demo_str.isnumeric())
print(demo_num.isnumeric())