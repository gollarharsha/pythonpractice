import re
fh = open("/Users/harshagolla/Desktop/python-practice-2018/Files/regex_sum_88526.txt")
all_list = []
total = 0
total1 = 0
count = 0
for line in fh:
    line.rstrip()
    stuff = re.findall("[0-9]+", line)
    if len(stuff) >0:
        for element in stuff:
            total = total + int(element)
            all_list.append(total)
            total = 0
for element1 in all_list:
    count = count + 1
    total1 = total1 + element1
print(count)
print(total1)
