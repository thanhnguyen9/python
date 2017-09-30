# https://www.hackerrank.com/challenges/mini-max-sum/problem


sorted_arr = sorted(arr)

print(sum(sorted_arr[0:4]), sum(sorted_arr[1:5]))

# Without sum method
# min = 0
# max = 0

# for i in range(0, 4):
# 	min += sorted_arr[i]
# 	max += sorted_arr[i+1]

# print(min, max)