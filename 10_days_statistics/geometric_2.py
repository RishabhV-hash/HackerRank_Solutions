p0 = list( map( float, input().strip().split(" ") ) )
n = int(input())

pf = p0[0] / p0[1]
p = pf
for i in range(1,n):
    p += (1-pf)**(i) * pf

print("%.3f" % p)