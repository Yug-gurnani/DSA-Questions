def maxRectangle(M, n, m):
    # code here
    def mah(arr,n):
        stack = []
        left = []
        right = []
        ans = []
        for i in range(n):
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1][1])
            stack.append([arr[i],i])
        stack = []
        for i in range(n-1,-1,-1):
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if not stack:
                right.append(n)
            else:
                right.append(stack[-1][1])
            stack.append([arr[i],i])
        right = right[::-1]
        for i in range(n):
            ans.append(right[i]-left[i]-1)
        currmax = 0
        for i in range(n):
            currmax = max(currmax,arr[i]*ans[i])
        return currmax
    curr_arr = M[0]
    temp = mah(curr_arr,len(curr_arr))
    areas = [temp]
    for i in range(1,n):
        for j in range(m):
            if M[i][j] == 0:
                curr_arr[j] = 0
            else:
                curr_arr[j] += M[i][j]
        temp = mah(curr_arr,len(curr_arr))
        areas.append(temp)
    return max(areas)
    