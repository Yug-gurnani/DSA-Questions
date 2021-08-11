def deleteNode(curr_node):
    #code here
    curr_node.data,curr_node.next.data = curr_node.next.data,curr_node.data
    if not curr_node.next.next:
        curr_node.next = None
        return
    deleteNode(curr_node.next)