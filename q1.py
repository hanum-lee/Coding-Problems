import re

def reverse(x:int) -> int:
    xstring = str(x)
    lastdigit = True
    if len(xstring) > 1:
        while(lastdigit):
            if (xstring[len(xstring) -1]) == "0":
                xstring = xstring[:len(xstring)-1]
            else:
                lastdigit = False
    if xstring[0] == '-':
        neg = xstring[1::]
        output = '-' + neg[::-1]
        
        return int(output)
    return(int(xstring[::-1]))
    
print(reverse(0))

if 9646324351 > (2 ** 31 - 1):
    print("Bigger")
else:
    print("false")