import numpy as np


"""
array( (1, 2, 3) )  /// список объявляется в квадратных скобках, а кортеж — в круглых
array( [1, 2, 3] )  ///
"""

#a = np.array([1, 2, 3, 4], 'float64')
#print (np.sctypeDict)
#a = np.array([1, 2, 3, 4], 'uintc')
#a = np.array([1, 2, 3, 4], 'str_')
#a = np.complex64(10)
#a = np.int16(10.5)
#a = np.array([1, 2, 5000, 1000], dtype='int8')
#a = np.array([1, 2, 5000, 1000])
#b = np.complex64(a)
#c = np.int32(b)

#a = np.array( [[1, 2], [3, 4], [5, 6]] )
#a = np.array( [[1, 2], [3, 4], [5, 6, 7]] )
a = np.array( [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]] )


#print (np.array( (1, 2, 3) ))
#print (np.array( 'Hello' ))
#print (a)
#print (c)

#print (a)

print (a[0,0,0])

#print (a[1])


