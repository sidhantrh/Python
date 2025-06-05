def modify(character,string):
    list_string = list(string)
    list_string[1] = character
    modified_string = " "
    for i in list_string:
        modified_string = modified_string + i
    return modified_string


def menu():
    string = input("Original String: ")
    print("Memory ID: ", id(string) )
    reversed_string = string[::-1]
    print("Reversed String: ", reversed_string)
    print("Modified String: ",  modify("x", reversed_string))
    
menu()
    
    