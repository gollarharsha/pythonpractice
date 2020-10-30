def reverseInteger(n):
    Flag =  None # Set the Flag
    nStr = str(n) # Convert it o String
    if nStr[0] == "-": # Take care of the sign
        nStr = nStr[1:]
        Flag = True
    rev = nStr[::-1] # Reverse it
    if Flag:
        rev="-"+rev
    # if rev > 2**31 - 1 or rev < -2**31:
    #     rev = 0
    return rev
print(reverseInteger(11213))