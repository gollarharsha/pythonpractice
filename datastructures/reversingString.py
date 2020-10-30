def reversingString(s):
    if len(s) == 0:
        return ""
    if len(s) ==1:
        return s
    return s[-1]+ reversingString(s[:-1])

print(reversingString("ars"))