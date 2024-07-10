import sys

iter = int(sys.stdin.readline())
start = 2
for i in range(iter):
    start = start + (start - 1)
num = start ** 2
print(num)
