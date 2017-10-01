# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def getRecord(s):
    # Complete this function
    highest_point = s[0]
    lowest_point = s[0]
    total_best = 0
    total_worst = 0
    
    for i in s:
        if i > highest_point:
            total_best += 1
            highest_point = i
        elif i < lowest_point:
                total_worst += 1
                lowest_point = i
                
    return (total_best, total_worst)