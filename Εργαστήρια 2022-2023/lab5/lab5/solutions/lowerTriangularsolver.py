import numpy as np

A = np.array( [ [1,0,0,0,0], [1,2,0,0,0], [1,2,3,0,0], [1,2,3,4,0], [1,2,3,4,5] ], dtype='float' )

b = np.array( [1,2,3,4,5], dtype='float' ).reshape( (-1,1) )
print( 'A' )
print( A )
print( 'b' )
print( b )

def lowerTriangularsolver( A, b ):
    x = np.zeros_like( b, dtype='float' )
    n = x.shape[0]

    for i in range( n ):
        s = 0
        for j in range( 0, i ):
            s += A[i][j] * x[j]     
        x[i] = ( b[i] - s ) / A[i][i]

    return x

def upperTriangularsolver( A, b ):
    ret = lowerTriangularsolver( A.T, b.T )
    return ret

print( 'x' )
x = lowerTriangularsolver( A, b )
print( x )
print( 'check' )
print( np.dot(A,x) )

print( 'Upper case' )
#we know that
#Ax=b| lower case
#x^T A^T = b^T#upper case

#In this example I choosed an array B = A^{T}
#and b2 = b^T
x2 = upperTriangularsolver( A.T, b.T )

print( 'x2' )
print( x2 )

print( 'check')
print( np.dot(x2.T,A.T) )

print( 'b2' )
print( b.T )