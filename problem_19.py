
if __name__ == '__main__':
    s = raw_input()
    string_length=len(s)
def alnum(s):
     for i in range (string_length):
        if (s[i].isalnum()):
            return True
            break
        return False
def alpha(s):
    for i in range (string_length):
        if (s[i].isalpha()):
            return True
            break
        return False
def digit(s):
    for i in range (string_length):
        if (s[i].isdigit()):
            return True
            break
        return False
def lower(s):
    for i in range (string_length):
        if (s[i].islower()):
            return True
            break
        return False
def upper(s):
    for i in range (string_length):
        if (s[i].isupper()):
            return True
            break
        return False

    
print(alnum(s))
print(alpha(s))
print(digit(s))
print(lower(s))
print(upper(s))
