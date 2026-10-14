# F-strings
name = "meet"

my_str = "Hello my name is meet, how are you"
my_str = f"Hello my name is {name}, how are you"

print(my_str)


# Try block - anything defined or the code inside try block is tried to run and failed it will simply jump to next code
# blocks and will not stop full code base to stop running

x = "10"

try:
    if(x>10):
        print("Greater than 10")
    else:
        print("IDK")

# This will only run if error occurs
except Exception as e:
    print(f"Error Caught - {e}")

finally:
    print("I will always even if error or no error occurs above")

print("Next code")
