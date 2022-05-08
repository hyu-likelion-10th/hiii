c = int(input())

for i in range(c):
    arr = list(map(int, input().split()))
    n = arr[0]
    avg = sum(arr[1:])/n
    cnt = 0
    for k in range(1, n+1):
        if arr[k]>avg:
            cnt+=1
    ans = cnt/n*100
    print(f"{ans:.3f}%")