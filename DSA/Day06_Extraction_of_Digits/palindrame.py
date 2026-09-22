#Q.In put any Palindrame  number  and show is palindrame or not .

n = int(input("Enter the Number : - "))

num = n
result = 0

while num > 0:
    last_num = num % 10
    result = (result * 10) + last_num
    num = num // 10

print(result)

if result == n :
    print("IT is Palindrame")
else:
    print("It is not Palindrame")


