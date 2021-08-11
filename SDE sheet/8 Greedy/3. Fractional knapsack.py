"""
Given weights and values of N items,
 we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 
"""
def fractionalknapsack(w,arr,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    # code zip(Items,W))
    arr.sort(key = lambda x:x.value/x.weight,reverse = True)
    ans = 0
    for i in arr:
        #print(i.value,i.weight,end = "")
        if i.weight < w:
            ans += i.value
            w -= i.weight
        else:
            ans += (w/i.weight) * i.value
            w = 0
            break
        #print(ans)
    #print()
    return ans
"""
TC = o(n*log n)
SC = o(1)
"""