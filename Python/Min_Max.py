import numpy
N,M = map(int,input().split())
my_array = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(my_array,axis=1)))
