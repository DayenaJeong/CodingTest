import sys

soil = int(sys.stdin.readline())
fert = list(map(int, sys.stdin.readline().split()))
product = []

for i in range(soil - 1):
    for j in range(soil - 1):
        if i != soil - j - 1:
            product.append(fert[i] * fert[soil - j - 1])

print(max(product))