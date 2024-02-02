import sys

total = 0
for i in range(5):
    time = list(sys.stdin.readline().split())
    ts1 = []
    for i in range(len(time)):
        ts1.append(time[i].split(":"))
    ts2 = sum(ts1, [])
    ts = list(map(int, ts2))

    if (ts[3] - ts[1]) >= 0:
        hour = ts[2] - ts[0]
        min = ts[3] - ts[1]
    else:
        hour = ts[2] - ts[0] - 1
        min = 60 + (ts[3] - ts[1])

    total_day = hour * 60 + min
    total += total_day

print(total)