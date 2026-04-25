# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2 
        res = cur = ListNode() 

        carry = 0
        while cur1 and cur2:
            print('a') 
            sum = cur1.val + cur2.val
            if carry == 1: 
                sum += 1
                carry = 0 
            if sum >= 10: 
                carry = 1 
                sum -= 10 
            cur.next = ListNode(sum)
            cur1, cur2, cur = cur1.next, cur2.next, cur.next 
        
        while cur1:
            print('A') 
            sum = cur1.val
            if carry == 1: 
                sum += 1 
                carry = 0 
            if sum >= 10: 
                carry = 1
                sum -= 10 
            cur.next = ListNode(sum)
            cur1, cur = cur1.next, cur.next
        
        while cur2: 
            print('B')
            sum = cur2.val 
            if carry == 1: 
                sum += 1 
                carry = 0 
            if sum >= 10: 
                carry = 1
                sum -= 10 
            cur.next = ListNode(sum)
            cur2, cur = cur2.next, cur.next

        if carry == 1:
            print('C') 
            cur.next = ListNode(1) 
        return res.next 