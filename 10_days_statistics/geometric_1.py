p0 = list( map( float, input().strip().split(" ") ) )
n = int(input())

pf = p0[0] / p0[1]

p = (1-pf)**(n-1) * pf

print("%.3f" % p)