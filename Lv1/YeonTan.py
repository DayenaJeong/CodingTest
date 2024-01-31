import sys

num = int(sys.stdin.readline())
village = list(map(int, sys.stdin.readline().split()))
distance = []
count = 0
for i in range(num-1):
    if village[i] - village[i+1] < 0:
        distance.append(village[i+1] - village[i])
    else:
        distance.append(village[i] - village[i+1])

for j in distance:
    if j == min(distance):
        count += 1

print(count)