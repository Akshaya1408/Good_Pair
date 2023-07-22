def good_pair(arr,b):
    length=len(arr)
    for i in range(length):
        for j in range(i+1,length):
            if arr[i]+arr[j]==b:
                return 1
    
    return 0
    
arr=list(map(int,input().split()))
b=int(input())
print(good_pair(arr,b))