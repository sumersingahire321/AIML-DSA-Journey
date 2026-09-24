#factor 
num = 20 
n = num 
result = [] # use in list formate 

for i in range(1, n+1):
    if n % i == 0 :
        print(i)
        result.append(i)

print(f"The factor numbers is {result} ") # Show in the lsit formate 



