from parserC import *
from typeC import *
from utl import *

def evac(parsed : list) -> str:
    "Solve the expresion Ax = b"

    for index,value in enumerate(parsed):
        if index < len(parsed)-1:
            if type(value) == type(fraction(1,1)) and type(parsed[index+1]) == type(variable("a")):
                parsed[index] *= parsed[index+1]
                parsed.pop(index+1)
    #merge fraction with varaible
    
    L = parsed[0:parsed.index('=')]
    R = parsed[parsed.index('=')+1:]

    #Find every variables
    Lcoef = addf([ i.coef for i in L if type(i) == type(variable("foo"))])
    Rcoef = addf([ i.coef*-1 for i in R if type(i) == type(variable("foo"))])
    Coef = Lcoef + Rcoef

    #Find every value
    Lval = addf([ i*-1 for i in L if type(i) == type(fraction(1,2)) or type(i) == type(1)])
    Rval = addf([ i for i in R if type(i) == type(fraction(1,2)) or type(i) == type(1)])
    Cval = Lval + Rval

    #solve
    answer = Coef.inverse()*Cval
    return ("{0} = {1}".format("x",answer))


