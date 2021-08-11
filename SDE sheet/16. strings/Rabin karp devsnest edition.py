s = "AAAAAAA"
t = "AAA"
a=l=len(t)
p = 26
hash_t = 0
for c in t:
    hash_t+= (ord(c)-96)*p**(l-1)
    l-=1
    
l=a 
i=0
hash_s=0

while l>0:
    hash_s+= (ord(s[i])-96)*p**(l-1)
    l-=1
    i+=1
flag = 1
if hash_t == hash_s:
    print("True")
    flag=0
    
while i<len(s):
    hash_s = (hash_s - (ord(s[i-a])-96)*p**(a-1))*p + ord(s[i])-96
    i+=1
    if hash_s == hash_t:
        flag = 0
        print("True")
            
if flag:
    print("False")

"""
TC = o(n+m)
"""