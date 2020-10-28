name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
new_dict = dict()
list1 = []
for line in handle:
    if line.startswith("From "):
        words = line.split()
        list1.append(words[1])
print(list1)
for word in list1:
    new_dict[word] = new_dict.get(word,0) + 1
bigCount = None
bigName = None
for name, count in new_dict.items():
    if bigCount is None:
        bigCount = count
    elif count > bigCount:
        bigCount = count
        bigName = name
print(bigName)
