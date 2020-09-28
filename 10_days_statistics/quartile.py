def x_median(data):
    if len(data)%2 == 0:
        return int(sum(data[len(data)//2-1:len(data)//2+1])/2)
    else:
        return data[len(data)//2]

def quartile(data, num):
    Q1 = x_median(data[:len(data)//2])
    Q2 = x_median(data)
    if num%2 == 0:
        Q3 = x_median(data[len(data)//2:])
    else:
        Q3 = x_median(data[len(data)//2+1:])
    return Q1,Q2,Q3
        
if __name__ == '__main__':
    n =int(input())
    data= sorted(list(map(int,input().strip().split())))
    Q1, Q2, Q3 = quartile(data,n)
    print (Q1)
    print(Q2)
    print(Q3)
