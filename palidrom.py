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
    return not(any([True for i in range(len(text)//2) if text[i].lower() != text[-i-1].lower()]))

#third solution 
def check_palidrom_three(text):
    '''
    check_palidrom(string)
    Argument: string
    Returns True if given string is a palindrome - string that you can read forehead or reverse with the same meaning eg. level, 101.  
    '''
    return (text[::-1]).lower() == text.lower()

print(check_palidrom_three("Sedses"))