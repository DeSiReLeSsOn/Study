a = list(map(int, input().split()))
b = list(map(int, input().split()))
n, m = len(a), len(b)
i, j = 0, 0 
res = []

while i < n and j < m:
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
while i < n:
    res.append(a[i])
    i += 1
while j < m:
    res.append(b[j])
    j += 1

print(*res)