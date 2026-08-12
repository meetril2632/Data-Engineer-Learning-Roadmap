firstName = "Meet"
lastName = "Poshia"
print(firstName+lastName)

# or declare like this x, y, z = 10, 5, 20
# If all variables have same value then declare like this -> x = y = z = 10
x=10
y=5
z="20"

print(firstName, x)
print(firstName, z)

print(x+y)

# To print/concatenate the two different type of data type you need to force convert into one like here we do z into string
print(z+firstName)

# the backslash allows us for python to read that +50+10+30 is also part of the above line of code or brackets ( ) also works
sum = 10+20+30+10+25+40\
      +50+10+30

sum = (10+20+30+10+25+40
      +50+10+30)

# typecast the variable value into other data type
a = 10
b = "10" # or a_new = str(a)
b_new = int(b)