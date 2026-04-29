s = "programming"

count = 0
vowels = "aeiouAEIOU"

for ch in s:
    if ch in vowels:
        count = count + 1

print("Vowels:", count)