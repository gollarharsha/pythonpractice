new_dict = {}
fh = open("harsha.txt", "r+")
for line in fh:
    words = line.split()
    for word in words:
        '''Creating a dict and corresponding number of times each word is repeated'''
        new_dict[word] = new_dict.get(word,0)+1
print(new_dict)
