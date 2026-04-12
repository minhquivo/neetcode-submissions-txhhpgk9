# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head 
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        
        prev, curr = None, slow.next 
        while curr: 
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        
        slow.next = None 
        first, second = head, prev

        while second: 
            temp1, temp2 = first.next, second.next 
            first.next = second 
            second.next = temp1 
            first, second = temp1, temp2
        
            