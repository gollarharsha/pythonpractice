fh = open("mbox-short.txt")
new_dict = dict()
for line in fh:
    words = line.split()
    for word in words:
        new_dict[word]=new_dict.get(word,0)+1

bigCount = None
bigWord = None

#Finding bigWord
for word,count in new_dict.items():
    if bigCount is None:
        bigCount=count
    elif count > bigCount:
        bigCount = count
        bigWord = word
