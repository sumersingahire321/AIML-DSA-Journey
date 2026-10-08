num = [1,2,3,3,5,6,7,7,8,8,4,3,2,1,9,3]
m = [1,32,3,45,-2,8,9,3,4,6,7,8,88,99,7]

N = int(input("Enter the number in the m list :- "))

h_f = {}
n = len(num)

for i in range(0,n):
    if num[i] in h_f:
        h_f[num[i]] += 1
    else:
        h_f[num[i]] = 1

if N in m:
    if N in h_f:
        print(h_f[N])
    else:
        print(0)
else:

    print("Please enter the correct number!")
print(h_f)

'''output
Enter the number in the m list :- 3
4
{1: 2, 2: 2, 3: 4, 5: 1, 6: 1, 7: 2, 8: 2, 4: 1, 9: 1}'''