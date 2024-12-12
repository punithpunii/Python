word=input("Enter the word:")
vow="aeiouAEIOU"
res=""
for c  in word:
    if c not in vow:
        res+=c
print(res)
