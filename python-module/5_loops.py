my_list = ["OrDer", "CustOMERs", "ProDUCts"]

for i in my_list:
    print(i)

for i in range(1, 11):
    print(i) # Prints 1 to 10

for i in my_list:
    if(i.lower() == "order"):
        print("Table Order")
    else:
        print("No Table Order")

for i in my_list:
    print(i)
    for j in i:
        print(j)    