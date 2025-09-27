import numpy as np
"""a = np.array([1, 2, 3, "4"])
print (a)
print (a.dtype)
a[0] = '1234'
print (a[0], a[2] )
"""
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print (a)
#a = a[ [2, 2, 3, 2, 2, 2, 2, 2, 2] ] 
#print (a)
#a = a[ [True, True, 1, False, False, False, False, False, False] ] 
#print (a)
b = a.reshape(3, 3)
print (b)
print (b[1, 2])
print (b[[1],[2]])