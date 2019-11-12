from typeC import fraction


def addf(a : list):
    total = fraction(0,1)
    for i in a :
        total += i
    return total

letter = [chr(i) for i in range(ord('a'),ord('z')+1)] + [chr(i) for i in range(ord('A'),ord('Z')+1)]


