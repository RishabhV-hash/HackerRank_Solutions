arr = []
for _ in range(6):
     arr.append(list(map(int, input().rstrip().split())))

glassum = []

'''
Brute force
for i in range(len(arr)-2):
    for j in range(len(arr)-2):
        glassum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
print(max(glassum)) '''

def hourglassSum(arr):
    maximum = -64 #since arr[i][j] varies from -9 to 9 therefore  sum lies from -63 to 63
    i = 0
    j = 0
    while i < 4 :
        temp = arr[i][j] + arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1] + arr[i+2][j]+arr[i+2][j+1]+ arr[i+2][j+2]
        if temp > maximum:
            maximum = temp
        j +=1
        if j == 4:
            j = 0
            i +=1
    return maximum

print(hourglassSum(arr))