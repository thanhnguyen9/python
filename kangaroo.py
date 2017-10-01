# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    total1 = x1
    total2 = x2
    if x1 > x2 and v1 > v2: 
        return 'NO'
    elif x2 > x1 and v2 > v1:
        return 'NO'
    else:
        i = 1
        while i < 10000:
            total1 +=  v1
            total2 +=  v2
            if total1 == total2:
                return 'YES'
            i += 1
            
    return 'NO'  