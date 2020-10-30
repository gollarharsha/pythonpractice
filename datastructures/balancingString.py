# def balancing(inputstring):
#     braces= {
#         "[":"]",
#         "{":"}",
#         "(":")"
#     }

  
#     status = None
#     iString = [ele for ele in inputstring]
#     countDict = {ele:iString.count(ele) for ele in iString}
#     for i,j in braces.items():
#         try:
#             if countDict[i] != countDict[j]:
#                 status = False
#                 break
#             else:
#                 status = True
#         except:
#             status = False
#     return status
    
        
        
        
    #     for i,j in zip(openlist,closelist): #looping over each pair of braces
    #         if i in countDict.keys():
    #             print(countDict[i], countDict[j])
    #             if countDict[i] == countDict[j]:
    #                 countDict.pop(i)
    #                 countDict.pop(j)
    #                 continue
    # except:
    #     pass
    # if len(countDict) == 0:
    #     return True 
    # else:
    #     return False


def balancing(inputstring):
    braces= {
        "[":"]",
        "{":"}",
        "(":")"
    }
    i = 0
    stack = []
    while i < len(inputstring):
        parameter = inputstring[i]
        if parameter in "({[":
            stack.append(parameter)
        else:
            if len(stack) >0:
                top = stack.pop()
                if is_match(parameter,top):
                    return True
            else:
                return False
        i+=1

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


print(balancing("(())}}[][{{}}{{"))


