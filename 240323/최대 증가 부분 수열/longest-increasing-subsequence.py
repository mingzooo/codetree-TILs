n = int(input())

arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if (arr[j] < arr[i]):
            dp[i] = max(dp[i], dp[j]+1)
        continue

print(max(dp))