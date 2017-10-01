# https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n, ar):
    # Complete this function
    pairs = []
    result = 0
    
    for i in ar:
        if i in pairs:
            result += 1
            pairs.remove(i)
        else:
            pairs.append(i)
            
    return result