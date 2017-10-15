# https://www.hackerrank.com/challenges/apple-and-orange/problem

def check(start_point, end_point, list, position):
    count = 0
    
    for element in list:
      diff = position + element
      if diff in range(s,t+1):
        count += 1
    return count

apple_count = check(s, t, apple, a)
orange_count = check(s, t, orange, b)
        
print(apple_count)
print(orange_count)