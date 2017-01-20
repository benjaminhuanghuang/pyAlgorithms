'''
Dynamic Array


'''

# n, q = map(int, raw_input().strip().split(" "))
n = 2
q = 5
seq_list = [[] for i in range(n)]
last_ans = 0
for i in range(q):
    # n, q = map(int, raw_input().strip().split(" "))
    option = 1
    x = 0
    y = 5
    if option == 1:
        i = (last_ans ^ x) % n
        seq_list[i].append(y)
    elif option == 2:
        i = (last_ans ^ x) % n
        last_ans = seq_list[i][y % len(seq_list[i])]
        print last_ans
