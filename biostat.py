def mean(lst):
    '''
    Returns the mean of a given iterable of numbers.
    '''
    
    return(sum(lst)/len(lst))

def var(lst):
    x=[]
    for i in lst:
        x.append((i-mean(lst))**2)
    return(sum(x)/(len(lst)))

def std(lst):
    return(var(lst)**0.5)

#print(mean([1,2,3]))
