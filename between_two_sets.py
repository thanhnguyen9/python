# https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
    # Complete this function
    i = 1
    count = 0
    while i < 101:
        if aConditionChecking(i, a) and bConditionChecking(i, b):
           count += 1
        i += 1
    return count

def aConditionChecking(i, a):
    for a_element in a:
        if i % a_element != 0:
            return False
    return True

def bConditionChecking(i, b):
    for b_element in b:
        if b_element % i != 0:
            return False
    return True