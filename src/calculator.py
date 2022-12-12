


def sum(a,b):
    return a+b

def subtraction(a,b):
    return round(a-b,1)

def multip(a,b):
    if type(a) == str or type(b) == str:
            raise TypeError
    else:
        return a*b