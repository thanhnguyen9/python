# https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    total = 0
    
    for k in keyboards:
        for d in drives:
            if k + d > total and k + d <= s:
                total = k + d
                
    if total == 0:
        return -1
    else:
        return total   