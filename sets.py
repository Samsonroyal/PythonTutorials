my_set.add("anything")
print(my_set)
#adding items from another set
other_set = {8, 6, 10, "benjamin"}
my_set.update(other_set)
print(my_set)
other_list = [2, 55, 78, "Fred"]
my_set.update(other_list)
print(my_set)
my_set.update(("winnie", "ozzy"))
print(my_set)
my_set.update("bob", "ushinde")
print(my_set)