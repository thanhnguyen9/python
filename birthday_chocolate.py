# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def solve(n, s, d, m):
    # Complete this function
    result = 0
    for i in range(0, len(s)-m+1):
        total = s[i]
        
        for j in range(1,m):
            total += s[i+j]
            
        if total == d:
            result += 1
    
    return result