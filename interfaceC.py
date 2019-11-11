import itertools

from parserC import *
from typeC import *
from evalC import *

def get_user_input(): # generator function
    for i in itertools.count(): # infinite loop
        try:  
            yield i , input ('In [%d] ' % i) # return without ending the function
        except KeyboardInterrupt:
            break
        except EOFError:
            break

def main():
    for i , user_input in get_user_input():
        print(('Out[%d] ' % i) + evac(parse(user_input)))
    


if __name__ == "__main__":
    main()