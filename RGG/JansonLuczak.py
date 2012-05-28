'''
Created on 24.05.2012

@author: berlioz

This is RGG v. 1.0.
@input: number of vertices, power of the model
@output: graph
'''

import numpy as np
import utils    

# number of vertices
n = 1000000

# power of the model
beta = 1.7

# average degree of the graph
mean_degree = 1000

# generate a power-law array with defined parameters
powerLawArray = utils.powelawArray(n, beta, mean_degree)

# as stated in Chung-Lu article we create an array of ints just taking the lower bound of the values
# from the power-law sequence

#powerLawDegreeSequence = [0]*n
powerLawDegreeArray = np.array(powerLawArray, dtype = np.longlong)
print powerLawDegreeArray.size


# counter. sumOfDegrees = Sum_i d_i
sumOfDegrees = powerLawDegreeArray.sum()
print sumOfDegrees


# array of delimiters
delimiterArray = np.cumsum(powerLawDegreeArray)
delimiterArray = np.insert(delimiterArray, 0, 0) #adding 0 to the beginning
delimiterArray = np.delete(delimiterArray, n) # final edition of delimiterArray

#print delimiterArray[678]
#print delimiterArray[679]
print np.searchsorted(delimiterArray, delimiterArray[678] + 1) #defines number of vertex to which picked dot corresponds
print '\n'
#print delimiterArray[n-1]
#print np.searchsorted(delimiterArray, delimiterArray[n - 1] + 1)






