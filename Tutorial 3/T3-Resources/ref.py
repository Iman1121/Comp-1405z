def isvalid(string):
    reverse_string = string[::-1]

    bracketList = ['(', '{', '[']
    reverseBracketList = [')', '}', ']']

    for x in string:
        count = 0
        if(x in bracketList):
           
            for y in reverse_string:
                count += 1
                if(y in reverseBracketList):
                   
                    if(reverseBracketList.index(y) == bracketList.index(x)):      
                        reverse_string = reverse_string[0:count-1] + reverse_string[count:]                        
                        break
                    else:
                        return False  
                else:
                    return False
        else:
            return False        
    return True
print(isvalid("((x * x) + 2x) - (3 - (2 * 4) + (4 + (3 * (2 + 1))))"))
#{{[()(){[]()}]}((([{()[]{}}])))}
#((x * x) + 2x) - (3 - (2 * 4) + (4 + (3 * (2 + 1))))
    # for x in string:
    #     count = 0
    #     if(x=="{" or x=="(" or x=="["):
    #         for y in reverse_string:
    #             count += 1
    #             if(y=="}" or y==")" or y == "]"):
    #                 if(y==")" and x=="("):                        
    #                     reverse_string = reverse_string[0:count-1] + reverse_string[count+1:]                        
    #                     break
    #                 if(y == "}" and x =="{"):
    #                     reverse_string = reverse_string[0:count-1] + reverse_string[count+1:]
    #                     break
    #                 if(x == "[" and y =="]"):
    #                     reverse_string = reverse_string[0:count-1] + reverse_string[count+1:]
    #                     break
    #                 else:
    #                     return False  
    # return True



