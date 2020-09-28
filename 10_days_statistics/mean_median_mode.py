def x_mean(data):
    return sum(data)/len(data)

def x_median(data):
    n = len(data)
    index = n//2
    if n%2:
        return sorted(data)[index]
    else:
        return sum(sorted(data)[index- 1:index+1])/2

def x_mode(data):
    mode = max(sorted(data), key=data.count)
    return mode
if __name__ == '__main__':
    n = int(input())
    data = list(map(int,input().strip().split()))[:n]
    print(x_mean(data))
    print(x_median(data))
    print(x_mode(data))
