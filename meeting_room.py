import sys

r_num, m_num = map(int, sys.stdin.readline().split())

r_list = []
inform = []
for i in range(r_num):
    r_list.append(sys.stdin.readline().rstrip('\n'))
r_list.sort()

for j in range(m_num):
        inform.append(list(sys.stdin.readline().split()))
#print(inform)
for i in range(r_num):
    t_list = []
    for j in range(m_num):
        if inform[j][0] == r_list[i]:
            t_list.append(int(inform[j][1]))
            t_list.append(int(inform[j][2]))
    t_list.sort()
    #print(t_list)
    print(f'Room {r_list[i]}:')
    if len(t_list) == 0:
        print("1 available:")
        print("09-18")
    else:
        if t_list[0] == 9:
            t_list.remove(9)
        else:
            t_list.insert(0, '09')
        if t_list[-1] == 18:
            t_list.remove(18)
        else:
            t_list.append(18)
        t_list_result = []
        for value in t_list:
            if value not in t_list_result:
                t_list_result.append(value)
            else:
                t_list_result.remove(value)  
        if len(t_list_result) > 0:
            print(f'{int(len(t_list_result)/2)} available:')
            for k in range(len(t_list_result)):
                if (k+1) % 2 != 0:
                    print(f'{t_list_result[k]}-{t_list_result[k+1]}') 
        else:
            print("Not available")
    if i != (r_num-1):
        print("-----")
