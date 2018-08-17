list1 = [2,3,5,8,9,22,33]
count = 0
sum = 0
print("index", "number", "running_total")
for element in list1:
    count = count + 1
    sum = sum + element
    print(count, element, sum)
print(sum)
