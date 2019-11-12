def gcd(a,b):
    """
    This a modern implementation of Euclide's algorithm using modulus operator
    """
    a =  abs(a)
    b =  abs(b)
    while b > 0:
        a,b = b , a % b
    return a


class fraction(object):
    def __init__(self,num,den):
        div = gcd(num,den)
        if den != 0 :
            if (den < 0):
                self.num = -1*num//div
                self.den = -1*den//div
            else:
                self.num = num//div
                self.den = den//div
        else:
            raise ZeroDivisionError
    def __str__(self):
        if self.den != 1 :
            return "{0}/{1}".format(self.num,self.den)
        else:
            return "{0}".format(self.num)
    def __mul__(self,other):
        if type(other) == type(self):
            return fraction(self.num * other.num , self.den * other.den)
        elif(type(variable('x')) == type(other)):
            if (self.num == 0 ):
                return 0 
            elif(type(other.coef) != type(self)):
                other.coef =fraction(other.coef,1)*self
                return other
            else:
                other.coef =other.coef *self
                return other
        elif(type(other) == type(0)):
            other=fraction(other,1)*self
            return other 
        elif(type(other) == type(1.0)):
            return (self.num/self.den)*other
        else:
            raise Exception
    def inverse(self):
        return fraction(self.den,self.num)
    def __truediv__(self,other):
        if type(other) == type(self):
            return self * other.inverse()
        else:
            raise Exception
    def __add__(self,other):
        if type(self) == type(other):
            return fraction(self.num*other.den + other.num*self.den,self.den*other.den)
        elif(type(other) == type(1)):
            return fraction(other,1) + self
        else:
            raise Exception

class variable(object):
    def __init__(self,name):
        self.name = name
        self.coef = 1
        self.value = None
    def __str__(self):
        if self.value == None:
            if self.coef != 1:
                return '{0}{1}'.format(self.coef,self.name)
            else:
                return self.name
        else:
            return self.value
    def __mul__(self,other):
        if (type(fraction(1,1)) == type(other)):
            if(other.num == 0):
                return 0
            else:
                self.coef = fraction(self.coef,1)*other
        elif(type(other) == type(1) or type(other) == type(1.0)):
            if (other == 0):
                return 0 
            else:
                self.coef *= other
        else:
            raise Exception