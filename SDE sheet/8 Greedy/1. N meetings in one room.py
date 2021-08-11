"""
There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) 
where S[i] is start time of meeting i and F[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room
when only one meeting can be held in the meeting room at a particular time? 
Also note start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
"""
def maximumMeetings(n,start,end):
    # code here
    arr = list(zip(start,end))
    arr.sort(key = lambda x:x[1])
    cnt = 0
    prev = arr[0]
    for i in range(1,n):
        if prev[1] < arr[i][0]:
            prev = arr[i]
        else:
            cnt += 1
    return n - cnt
"""
TC = o(n*log(n))
SC = o(n)
"""