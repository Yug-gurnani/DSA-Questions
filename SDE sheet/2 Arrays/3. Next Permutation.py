"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Input: nums = [1,2,3]
Output: [1,3,2]
"""

def nextPermutation(self, arr: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def rev(arr):
        n = len(arr)
        l = 0
        r = n-1
        while l < r:
            arr[l],arr[r] = arr[r],arr[l]
            l += 1
            r -= 1
        return arr
    flag = False
    n = len(arr)
    for i in range(n-1,0,-1):
        #print(arr[i],arr[i-1])
        if arr[i] > arr[i-1]:
            flag = True
            for j in range(i,n):
                if arr[j] > arr[i-1]:
                    res = j
            arr[i-1],arr[res] = arr[res],arr[i-1]
            arr[i:] = rev(arr[i:])
            return arr
    if not flag:
        arr.sort()
        return arr
"""
TC = o(n)
sc = o(1)
"""