# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    # Complete this function
    count = 0
    for i in range(0,len(ar)-1):
    	for j in range(i+1, len(ar)):
    		total = ar[i] + ar[j]
    		if total % k == 0:
    			count += 1
    return(count)