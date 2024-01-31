import sys

len = int(sys.stdin.readline())

for i in range(len):
    a = list(map(int, sys.stdin.readline().split()))
    print(f"Case #{i+1}: {a[0]+a[1]}")