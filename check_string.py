if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    
    res = list(s)
    
    for i in res:
        if i.isalnum():
            alnum = True
            break
            
    for i in res:
        if i.isalpha():
            alpha = True
            break
    
    for i in res:
        if i.isdigit():
            digit = True
            break
            
    for i in res:
        if i.islower():
            lower = True
            break
            
    for i in res:
        if i.isupper():
            upper = True
            break
        
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
            