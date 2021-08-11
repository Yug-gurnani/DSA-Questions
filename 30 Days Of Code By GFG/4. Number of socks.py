"""
A drawer contains socks of n different colours.
The number of socks available of ith colour is given by a[i] where a is an array of n elements.
Tony wants to take k pairs of socks out of the drawer. However, he cannot see the colour of the sock that he is picking.
You have to tell what is the minimum number of socks Tony has to pick in one attempt from the drawer
such that he can be absolutely sure, without seeing their colours, that he will have at least k matching pairs.

Example 1:

Input: N = 4, a[] = {3, 4, 5, 3}, K = 6
Output: 15
Explanation: The worst case scenario, after 
14 picks will be 3,3,3,3 or 3,1,5,3 where 
each number represents picks of socks of 
one colour. Hence, 15th pick will get the 
5th pair for sure.


First you should calculate maximum no. of pairs that can be formed.

Then check if k > max_pairs then return -1;

because k pairs cannot be formed.

Then take out maximum pairs without exhausting any color and storing it in a variable 'sum', means that if there are 6 socks of a color then you should consider only 2 pairs (because if you will take out 3 pairs then all socks will be exhausted).

Now, if k>sum :
'sum' pairs were picked already, so no. of socks picked = 2*sum
as sum pairs are not enough (i.e, not equal to k), so we need to take more socks, then we will take n more socks (i.e, 1 sock from each color), so now each color will have 1 or 0 sock remaining, then each new pick will complete a pair, therefore (k-sum) more picks are required

and if k <= sum :

let 'k-1' pairs are picked using 2*(k-1) socks, then you will take n pairs more (of unique colors) and if we will take one more pair it will complete the kth pair 
"""
def find_min(self, a, n, k):
    maxpairs = 0
    s = 0
    for i in range(n):
        maxpairs += a[i] // 2
        if a[i] % 2 == 0:
            s += a[i] // 2 - 1
            a[i] = a[i] - (a[i]//2-1)*2
        else:
            s += a[i] // 2
            a[i] = a[i] - (a[i]//2)*2
    if k > maxpairs:
        return -1
    if k > s:
        ans = s * 2
        ans += n
        ans += k-s
        return ans
    else:
        return 2 * (k-1) + n + 1
"""
TC = o(n)
SC = o(1)
"""