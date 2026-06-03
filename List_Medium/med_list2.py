n = int(input())
arr =  list(map(int,input().split()))
k = int(input())
rest = arr[:-k]
last = arr[-k:]
print(last + rest)
