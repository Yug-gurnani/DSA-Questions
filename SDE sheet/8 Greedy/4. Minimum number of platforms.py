"""
Given arrival and departure times of all trains that reach a railway station.
Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day.
Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other.
At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms,

"""
def solve(arr,dep,n):
    arr.sort()
    dep.sort()
    i = 1
    j = 0
    pf = 1
    ans =1
    while i < n and j < n:
        if arr[i] <= dep[j]:
            i += 1
            pf += 1
            ans = max(ans,pf)
        else:
            pf -= 1
            j += 1
    return ans