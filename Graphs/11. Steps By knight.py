"""
This problem can be seen as shortest path in unweighted graph. Therefore we use BFS to solve this problem. 
We try all 8 possible positions where a Knight can reach from its position. 
If reachable position is not already visited and is inside the board, we push this state into queue with distance 1 more than its parent state. 
Finally we return distance of target position, when it gets pop out from queue.

Below code implements BFS for searching through cells, where each cell contains its coordinate and distance from starting node. 
In worst case, below code visits all cells of board, making worst-case time complexity as O(N^2).
"""
def minStepToReachTarget(k, t, n):
    '''
    knightpos: (x,y) tuple of current position coordinate
    targetpos: (x,y) tuple of target position coordinate 
    N: size of board
    
    return: minimum steps the Knight will take to reach the target position
    '''
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    visited = [[False for i in range(n+1)]for i in range(n+1)]
    queue = deque([[k[0],k[1],0]])
    visited[k[0]][k[1]] = True
    while queue:
        curr = queue[0]
        dist = curr[2]
        if curr[0] == t[0] and curr[1] == t[1]:
            return dist
        for i in range(8):
            x = curr[0] + dx[i]
            y = curr[1] + dy[i]
            if isInside(x,y,n) and not visited[x][y]:
                visited[x][y] = True
                queue.append([x,y,dist + 1])
        queue.popleft()