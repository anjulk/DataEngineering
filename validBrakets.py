# This code helps to find the valid brakets
def isValid(s):
    l = len(s)
    empty = []
    for i in range(l):
        if s[i] == '(' or s[i] == '{'  or s[i] == '[':
            empty.append(s[i])
        elif s[i] == ')' and '(' in empty:
            if empty[-1] == '(':
                empty.pop()
        elif s[i] == '}' and '{' in empty:
            if empty[-1] == '{':
                empty.pop()
        elif s[i] == ']' and '[' in empty:
                if empty[-1] == '[':
                    empty.pop()
        else:
            return False
    
    if empty == []:
        return True
    else:
        return False
        
        

print(isValid("[()]}"))
