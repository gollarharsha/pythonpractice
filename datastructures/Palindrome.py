def isPalindrome(iStr):
    if len(iStr)<=1:
        return True
    if iStr[0] == iStr[len(iStr)-1]:
        return isPalindrome(iStr[1:len(iStr)-1])
    return False
print(isPalindrome("madam"))