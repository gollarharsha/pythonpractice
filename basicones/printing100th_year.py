import datetime
now = datetime.datetime.now()
name = input("Enter your name: ")
age1 = input("Enter your current age:")
age = int(age1)
year = now.year

output = (100-age)+year

final_output = ("\n" + name + " will be celebrating 100th year during "+ str(output)+
"\n")
print(final_output)
x = input("How many times do you want above output to be printed")
x1 = int(x)
print(x1*final_output )
