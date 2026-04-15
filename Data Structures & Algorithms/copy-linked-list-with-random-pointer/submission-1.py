"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head 
        old_to_copy = {None : None}
        headCopy = Node(head.val)
        old_to_copy[head] = headCopy
        
        curr = head.next
        copy = headCopy  
        while curr:
            copy.next = Node(curr.val)
            old_to_copy[curr] = copy.next
            copy = copy.next 
            curr = curr.next 
        
        curr, copy = head, headCopy
        while curr: 
            if not curr.random: 
                copy.random  = None
            else:
                copy.random = old_to_copy[curr.random]
            copy = copy.next 
            curr = curr.next
            print(1)


        return headCopy