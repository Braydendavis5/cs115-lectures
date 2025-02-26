my_list = (5,5, "my age", 5.67)
print(type(my_list))

my_list = [[100,200],[300,4]]

print(my_list[0])
print(my_list[3])

my_list.append("milk")
print(my_list)

#access first character in string
print(my_list[0][0])

#remove from string
my_list.remove(5)
print(my_list)
my_list.pop(2)
print(my_list)

#get length of list
print(len(my_list))