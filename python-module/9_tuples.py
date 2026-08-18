# Tuples are same as lists so both of them are convertible to each other easily when required
my = () # empty tuple
my_tup = (1,2,3,4,5)

my_tuplist = list(my_tup) # Converted my_tup into list named my_tuplist
my_tuplist.append(6)

my_tup = tuple(my_tuplist) #Converts my_tuplist list into tuple
