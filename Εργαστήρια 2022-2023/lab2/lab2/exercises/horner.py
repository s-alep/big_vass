import numpy as np

a = np.array( [ [ 3, 0, -2, 0, 1, 0 ] ] ).T
x0 = -2
print(a.shape[0])


def horner( a, x0 ):
    for i in range (1):
        if i == 0:
            result = a[i]
        else:
            result = a[i] + result*x0

    return result  
        
        
print (a)
print( horner( a, x0 ) )
