#Write a function to return whether a number is palindrom or not
def palindrom(number):
    x=str(number)
    l = len(x)
    pd = True
    for i in range(l):
        if i >= int(l/2):
            if(x[i] != x[l-i-1]):
                pd = False
                break
    
    return pd
