if  __name__ == '__main__':
    n = int(input())
    X = list(map(int,input().strip().split()))[:n]
    W = list(map(int,input().strip().split()))[:n]
    weighted_sum = 0
    for i in range(n):
        weighted_sum += X[i]*W[i]
    weighted_mean = weighted_sum/sum(W)
    print(float(round(weighted_mean,1)))
