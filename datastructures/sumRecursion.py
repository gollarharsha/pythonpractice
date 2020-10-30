def sumofelements(testVariable):
    if testVariable == "":
        return 0
    return int(testVariable[0])+ sumofelements(testVariable[1:])

print(sumofelements("345"))