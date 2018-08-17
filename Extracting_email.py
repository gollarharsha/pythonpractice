fh = open("mbox-short.txt")
emails_list = []
emails = dict()
for line in fh:
    if line.startswith("From"):
        words = line.split()
        emails_list.append(words[1])

for element in emails_list:
    emails[element] = emails.get(element,0) + 1
print(emails)
