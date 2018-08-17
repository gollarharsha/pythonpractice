fh = open("mbox-short.txt")

new_dict = dict()

for line in fh:
    words = line.split()
    for word in words:
        new_dict[word] = new_dict.get(word,0)+1

'''bigWord = None
for word, count in new_dict.items():
    if bigCount is None or count>bigCount:
        bigCount = count
        bigWord = word

print(bigCount)
print(bigWord)'''

bigCount = None
bigWord = None
for word, count in new_dict.items():
    if bigCount is None:
        bigCount = count
    elif count > bigCount:
        bigCount = count
        bigWord = word
print(bigCount,bigWord)

smallCount = None
smallWord = None
for word, count in new_dict.items():
    if smallCount is None:
        smallCount = count
    elif count < smallCount:
        smallCount = count
        smallWord = word
print(smallCount,smallWord)
