import sys

a, b, d = map(int, sys.stdin.readline().split())
if a < d:
    f_iter = d // a
    f_remain = d % a
    f_time = f_iter * (a + b) + f_remain

    s_iter = d // b
    s_remain = d % b
    s_time = s_iter * (a + b) + s_remain

    t_time = f_time + s_time

elif a >= d:
    iter = d // b
    remain = d % b
    t_time = a + iter * (a + b) + remain

print(t_time)