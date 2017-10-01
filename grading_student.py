# https://www.hackerrank.com/challenges/grading/problem

def solve(grades):
    new_grades = []
    # Complete this function
    for i in range(0, len(grades)):
        if grades[i] < 38:
            new_grades.append(grades[i])
            continue
        
        if grades[i] % 5 == 0:
        	new_grades.append(grades[i])
        else:
        	new_number = grades[i] + (5 - grades[i] % 5)
	        if new_number - grades[i] < 3:
	            new_grades.append(new_number)
	        else:
	            new_grades.append(grades[i])
    
    return new_grades