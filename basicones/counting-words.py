no_of_lines = 0
no_of_words = 0

with open("sample.txt", "r+") as file:
    for line in file:
        no_of_lines = no_of_lines + 1
        new_element = line.split()
        for word in new_element:
            no_of_words = no_of_words + 1

print(no_of_lines)
print(no_of_words)
