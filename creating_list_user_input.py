user_list = []
l1 = input("Enter the length of list to be created")
l = int(l1)
count = 0

while count <= l:
    x = input("Enter the number to be appended in list ")
    user_list.append(x)
    count = count + 1

print(user_list)
