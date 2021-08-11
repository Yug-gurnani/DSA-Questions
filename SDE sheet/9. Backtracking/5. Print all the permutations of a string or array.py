"""
A permutation, also called an “arrangement number” or “order,” 
is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself.
A string of length n has n! permutation. 

Below are the permutations of string ABC. 
ABC ACB BAC BCA CBA CAB
"""
def permute(a,l,r):
    if l == r:
        print(a)
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i] = a[i],a[l]
a = ["a","b","c"]
permute(a,0,len(a)-1)
"""
TC = o(n * n!)
SC = o(1)
"""