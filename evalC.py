from parserC import *
from typeC import *

def evac(parsed : list) -> str:
    "Solve the expresion Ax = b"
    L = parsed[0:parsed.index('=')]
    R = parsed[parsed.index('=')+1:]
    #trivial algorith for solving the equation
    L = L[0]*L[1] # get only the variable on left side
    R = L.coef.inverse() * R[0]
    L = L.coef.inverse() * L
    return ("{0} = {1}".format(L.name,R))
