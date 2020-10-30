values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

# def romanInteger(s):
#     total=0
#     i=0
#     while i < len(s):
#         #print(values[s[i]],values[s[i+1]])
#         if i+1 < len(s) and values[s[i]] < values [s[i+1]]:
#             total += (values [s[i+1]] - values[s[i]])
#             i+=2
#             print("total", total)
#         else:
#             total +=values[s[i]]
#             i+=1
#     return total



def romanToInt(s):
    total= values.get(s[-1])
    for i in reversed(range(len(s)-1)):
        if values[s[i]] < values[s[i+1]]:
            total-=values[s[i]]
        else:
            total+=values[s[i]]
    return total

print(romanToInt("VXM"))
