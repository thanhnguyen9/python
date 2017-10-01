def bonAppetit(n, k, b, ar):
    
    ar[k] = 0
    total = sum(ar)
            
    bi=b-(total)//2
    
    if bi == 0:
        return 'Bon Appetit'
    return bi