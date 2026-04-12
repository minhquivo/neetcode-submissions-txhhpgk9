# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse:
        prev, curr = None, head 
        while curr: 
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp 
        
        #remove
        head = prev
        prev, curr = None, head
        count = 1 
        while count < n: 
            prev = curr 
            curr = curr.next
            count += 1
        
        if not prev:
            head = curr.next 
        else:
            prev.next = curr.next 
            curr.next = None 

        #reverse back
        prev, curr = None, head 
        while curr: 
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp

        return prev  