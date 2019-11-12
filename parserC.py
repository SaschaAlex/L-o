from typeC import *

Number = (int ,float,fraction)
Variable = variable
Symbol = str   
Atom   = (Symbol, Number)



space = lambda x : ' '+x if x in letter else x 
getting_var = lambda foo : "".join([space(i) for i in foo])

def tokenize(chars : str) -> list:
    "Convert a string of characters into a list of tokens"
    chars = getting_var(chars)
    return chars.replace('(', '( ').replace(')', ' )').replace('=' , ' = ').split()

def parse(program: str) -> list:
    "Read a scheme expression from a string."
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens : list) -> list:
    "Read an expression from a sequence of tokens"
    if len(tokens) == 0 :
        raise SyntaxError('Unexpected')
    token = tokens.pop(0)   # remove and return item ad index 0
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError('Unexpected ) ')
    else:
        return atom(token)

def atom(token: str) -> Atom:
    "Number becom numbers ; other token is a symbol."
    
    if len(token) >= 3 and  '/' in token:
        token = token.replace('/', ' ').split()
        try : return fraction(int(token[0]), int(token[1]))
        except ValueError:
            raise Exception("Invalid faction type")
    else:
        try : return fraction(int(token),1)
        except ValueError:
            try: return float(token)
            except ValueError:
                if token in letter:
                    return variable(token)
                else:
                    return Symbol(token)



