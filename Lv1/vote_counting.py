import sys

num = int(sys.stdin.readline())
for i in range(num):
    vote = int(sys.stdin.readline())
    five = vote // 5
    line = vote % 5
    for j in range(five):
        if line != 0:
            print("++++ ", end="")
        else:
            if j != five - 1:
                print("++++ ", end="")
            else:
                print("++++")
    for k in range(line):
        if k != line - 1:
            print("|", end="")
        else:
            print("|")