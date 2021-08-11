def towerofhonai(n,from_,to_,aux_):
    if n==1:
        print('move disk',1,'from rod',from_,'to rod',to_)
    else:
        towerofhonai(n-1,from_,aux_,to_)
        print('move disk',n,'from rod',from_,'to rod',to_)
        towerofhonai(n-1,aux_,to_,from_)
for _ in range(int(input())):
    n = int(input())
    towerofhonai(n,1,3,2)
    print(2**n - 1)

