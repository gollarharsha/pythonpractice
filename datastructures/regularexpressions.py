import re

#Python program to check that a string contains only a certain set of characters
def stringCheck(str):
    output = re.search('[a-zA-Z0-9.]', str)
    return bool(output)

print(stringCheck("*&%@#!}{"")"))

#Python program that matches a string that has an a followed by zero or more b's.

def stringCheck1(str):
    output = re.search('ab*', str)
    return bool(output)

print(stringCheck1("a"))

#Python program that matches a string that has an a followed by one or more b's

def stringCheck2(str):
    output = re.search('ab+', str)
    return bool(output)

print(stringCheck2("ab"))

# Python program that matches a string that has an a followed by zero or one 'b'
def stringCheck3(str):
    output = re.search('ab?', str)
    return bool(output)

print(stringCheck3("bac"))

#Python program that matches a string that has an a followed by three 'b

def stringCheck4(str):
    output = re.search('ab{3}', str)
    return bool(output)

print(stringCheck4("abbb"))

#Python program that matches a string that has an a followed by two to three 'b'
def stringCheck5(str):
    output = re.search('ab{2,3}', str)
    return bool(output)

print(stringCheck5("abbbb"))

#Python program to find sequences of lowercase letters joined with a underscore.
def stringCheck6(str):
    output = re.search('^[a-z]+_[a-z]+$', str)
    return bool(output)

print(stringCheck6("aab_cbbbc"))

# Write a Python program to find the sequences of one upper case letter followed by lower case letters
def stringCheck7(str):
    output = re.search('^[A-Z]+[a-z]+$', str)
    return bool(output)

print(stringCheck7("aaAA"))

#Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def stringCheck8(str):
    output = re.search('^a[a-zA-Z-09]+b$', str)
    return bool(output)

print(stringCheck8("aabb"))

#Python program that matches a word at the beginning of a string
def stringCheck9(str):
    output = re.search('^\w+', str)
    return bool(output)

print(stringCheck9("The Harsha is a happy person"))

#Python program that matches a word at the end of string, with optional punctuation.
def stringCheck10(str):
    output = re.search('\w+\S+$', str)
    return bool(output)

print(stringCheck10("The Harsha is a happy person."))

#Python program that matches a word containing 'z'
def stringCheck11(str):
    output = re.search('\w*z\w*', str)
    return bool(output)

print(stringCheck11("The Harsha is a happy person."))

#Python program that matches a word containing 'z', not at the start or end of the word
def stringCheck12(str):
    output = re.search(r'\w*z\w*', str)
    return output.group()

print(stringCheck12("zebra Harsza zebra"))

# Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
def stringCheck13(str):
    output = re.findall(r'^[a-zA-Z0-9_]+$', str)
    return output

print(stringCheck13("a Python_Exercises_1"))

#Python program where a string will start with a specific number
def stringCheck14(str):
    output = re.findall('^[0-9]+[a-zA-Z]+$', str)
    return output

print(stringCheck14("abc 123abc"))

#Python program to remove leading zeros from an IP address
def stringCheck15(str):
    output = re.sub(r'[0]+', "", str)
    return output

print(stringCheck15("001.0002.003.0034"))

#Python program to check for a number at the end of a string
def stringCheck16(str):
    output = re.compile(r'(?:\w+\d+)')
    return output.findall(str)

print(stringCheck16("abc abc123 abc"))
