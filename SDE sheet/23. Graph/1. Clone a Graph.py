"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

You cannot return the originl graph
"""
def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return
    dic = {}
    def solve(node):
        if not node:
            return
        nonlocal dic
        new = Node(node.val)
        dic[node] = new
        for i in node.neighbors:
            if i in dic:
                new.neighbors.append(dic[i])
            else:
                new.neighbors.append(solve(i))
        return new
    solve(node)
    return dic[node]
"""
TC = o(n)
SC = o(n)
"""
