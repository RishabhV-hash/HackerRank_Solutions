import math

def x_mean(data):
    return sum(data)/len(data)

def variance(data):
    n = len(data)
    mean = x_mean(data)
    deviations = [(x-mean) ** 2 for x in data]
    variance = sum(deviations)/n
    return variance

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().strip().split()))[:n]
    print(stdev(data))
