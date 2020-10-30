def recursiveLength(testVariable):
    if testVariable == "":
        return 0
    return 1 + recursiveLength(testVariable[1:])
print(recursiveLength("12345"))