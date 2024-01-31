import sys

num = int(sys.stdin.readline())
list1 = []
list2 = []

for i in range(num):
    xy = list(map(int, sys.stdin.readline().split()))
    list1.append(xy)
    list2.append(xy[1])

for j in list1:
    if j[1] == min(list2):
        print(j[0], j[1])