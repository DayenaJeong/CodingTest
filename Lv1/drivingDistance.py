import sys

car = list(map(int,sys.stdin.readline().split()))
if car[0] > car[1]:
    print("A")
elif car[0] < car[1]:
    print("B")
else:
    print("same")