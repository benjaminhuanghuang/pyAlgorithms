'''
Give an array of integers, we define its degree as the maximum frequency of any element in the array
'''

arr = [1,2,3,4,2,2,3]
arr = [1,2,2 ,3,1]
def d(arr):
    dic ={}
    for i in arr:
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] = 1

    sorted_dic = sorted(dic.items(), key=lambda x: x[1])
    res = 0
    for k, v in dic.items():
        if v == sorted_dic[-1][1]:
            res += 1

    return res

print d(arr)
