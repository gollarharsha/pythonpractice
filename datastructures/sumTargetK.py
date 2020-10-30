def find_sum(lst, n):
    found_values = {}
    for ele in lst: #Looping over list
        try:
            found_values[n - ele] #To see if the dictionary has complement, if not add it
            return [n - ele, ele] # If it exists, return the complement and 
                                    #the current iterable which makes up the target
        except:
            found_values[ele] = 0
    return False
if __name__ == '__main__':
    print(find_sum([1, 3, 2, 4], 6))
