
def stringgen(n:int) -> str:
    output = ''
    for n in range(n-1):
        output += "x"
    if n % 2 == 0 :
        output += "y"
    else:
        output += "x"
    return output
        
print(stringgen(7))