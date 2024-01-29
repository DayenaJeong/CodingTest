import sys


def bar(x):
    if x == '0':
        y = [1, 1, 1, 0, 1, 1, 1]
    elif x == '1':
        y = [0, 0, 1, 0, 0, 0, 1]
    elif x == '2':
        y = [0, 1, 1, 1, 1, 1, 0]
    elif x == '3':
        y = [0, 1, 1, 1, 0, 1, 1]
    elif x == '4':
        y = [1, 0, 1, 1, 0, 0, 1]
    elif x == '5':
        y = [1, 1, 0, 1, 0, 1, 1]
    elif x == '6':
        y = [1, 1, 0, 1, 1, 1, 1]
    elif x == '7':
        y = [1, 1, 1, 0, 0, 0, 1]
    elif x == '8':
        y = [1, 1, 1, 1, 1, 1, 1]
    elif x == 'a':
        y = [0, 0, 0, 0, 0, 0, 0]
    else:
        y = [1, 1, 1, 1, 0, 1, 1]
    return y


def switch(a, b):
    sum2 = 0
    for i in range(5):
        sum1 = 0
        for j in range(7):
            if a[i][j] == b[i][j]:
                c = 0
            else:
                c = 1
            sum1 += c
        sum2 += sum1
    return sum2


num = int(sys.stdin.readline().split()[0])
for i in range(num):
    fir, sec = map(str, sys.stdin.readline().split())
    first = []
    if len(fir) < 5:
        for j in range(5 - len(fir)):
            first.append([0, 0, 0, 0, 0, 0, 0])
        for k in fir:
            first.append(bar(k))
    else:
        for k in fir:
            first.append(bar(k))
    second = []
    if len(sec) < 5:
        for j in range(5 - len(sec)):
            second.append([0, 0, 0, 0, 0, 0, 0])
        for k in sec:
            second.append(bar(k))
    else:
        for k in sec:
            second.append(bar(k))
    print(switch(first, second))