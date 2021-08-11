def bTreeToClist(root):
    #Your code here
    def dfs(root,arr):
        if root.left:
            dfs(root.left,arr)
        arr.append(root)
        if root.right:
            dfs(root.right,arr)
        return arr
    arr = dfs(root,[])
    for i in range(1,len(arr)):
        arr[i-1].right = arr[i]
        arr[i].left = arr[i-1]
    arr[-1].right = arr[0]
    arr[0].left = arr[-1]
    return arr[0]