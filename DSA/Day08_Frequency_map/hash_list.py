num = [1,2,3,3,5,6,7,7,8,8,4,3,2,1,9,3]
m = [1,32,3,45,-2,8,9,3,4,6,7,8,88,99,7]

hash_list = [0] * 11

for n in num :
    hash_list[n] += 1

for num in m :
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])


print(hash_list)

'''output
2
0
4
0
0
2
1
4
1
1
2
2
0
0
2
[0, 2, 2, 4, 1, 1, 1, 2, 2, 1, 0]'''
