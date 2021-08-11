"""
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

Example 1:

Input:
N = 4
Petrol = 4 6 7 4
Distance = 6 5 3 5
Output: 1
Explanation: There are 4 petrol pumps with
amount of petrol and distance to next
petrol pump value pairs as {4, 6}, {6, 5},
{7, 3} and {4, 5}. The first point from
where truck can make a circular tour is
2nd petrol pump. Output in this case is 1
(index of 2nd petrol pump).
"""
def tour(lis, n):
    #Code here
    cap,deficit,start = 0,0,0
    for j in range(n):
        i = lis[j]
        cap += i[0] - i[1]
        if cap < 0:
            start = j+1
            deficit += cap
            cap = 0
    #print(cap,deficit)
    if cap - abs(deficit) >= 0:
        return start
    else:
        return -1
"""
TC = o(n)
SC = o(n)
"""