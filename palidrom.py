#first version of solution
def check_palidrom_first(text):
    for i in range(len(text)//2):
        if text[i].lower() != text[-i-1].lower():
            return False
    return True

#second version
def check_palidrom(text):
    '''
    check_palidrom(string)
    Argument: string
    Returns True if given string is a palindrome - string that you can read forehead or reverse with the same meaning eg. level, 101.  
    '''
    return any(False if text[i].lower() != text[-i-1].lower() else True for i in range(len(text)//2))

print((check_palidrom_first("Kajak")))

print((check_palidrom("Kajak")))

# print(check_palidrom_sec("112"))
# print(check_palidrom_sec("1"))