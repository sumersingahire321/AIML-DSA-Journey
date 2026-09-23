# This number is Armstrong or not 
n = 153
num = n 
total = 0
nod = len(str(n))

while num > 0 :
    id = num % 10 
    total = total + (id**nod)
    num = num // 10

if total == n:
    print(f" {n} is Armstrong ")
else:
    print(f" {n} is not Armstrong ")

#output :- 153 is Armstrong 