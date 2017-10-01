# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(n, ar):

    # Complete this function
    new_ar = sorted(ar)
    checked_type = []
    
    max = {'type': new_ar [0], 'count': 1}
    existing = {'type': new_ar [0], 'count': 1}
    
    for i in range(1, len(new_ar)):	
        if new_ar[i-1] != new_ar[i]:
            if existing['count'] > max['count']:
                max['type'] = existing['type']
                max['count'] = existing['count']
		
            existing = {'type': new_ar [i], 'count': 1}    
        else:
            existing['count'] += 1
            
    if existing['count'] > max['count']:
        max['type'] = existing['type']
        max['count'] = existing['count']
        
    return max['type']