def decimalToBinary(n):
    if n>1:
        return decimalToBinary(n //2) + decimalToBinary(n %2)
    else:
        return str(n)
print(decimalToBinary(34))