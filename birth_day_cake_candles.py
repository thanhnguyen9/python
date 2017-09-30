# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(n, ar):
    # Complete this function
    ar = sorted(ar)
    tallest = ar[-1]
    total = 1
    
    for i in range(1, len(ar)):
        if ar[-1-i] == tallest:
            total += 1
        else:
            return total
        
    return total