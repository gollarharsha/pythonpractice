
all_list = []
fh = open("harsha.txt", "r")
for line in fh:
    words= line.split()
    for word in words:
        all_list.append(word)
        print(word + " is repeated " + str(all_list.count(word)) + " times")
