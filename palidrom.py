#first version of solution
def check_palidrom(text):
    for i in range(len(text)//2):
        if text[i].lower() != text[-i-1].lower():
            return False
    return True

#second version
def check_palidrom_sec(text):
    return any(False if text[i].lower() != text[-i-1].lower() else True for i in range(len(text)//2))

print(check_palidrom_sec("Kajak"))
print(check_palidrom_sec("112"))
print(check_palidrom_sec("1"))