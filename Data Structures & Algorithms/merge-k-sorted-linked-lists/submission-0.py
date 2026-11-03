# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: 
            return None
        while len(lists) > 1: 
            merged_lists = [] 
            for i in range(0, len(lists), 2):
                if i+1 < len(lists): 
                    merged_lists.append(self.merge(lists[i], lists[i+1])) 
                else: 
                    merged_lists.append(lists[i])
            lists = merged_lists.copy()

        return lists[0] 


    def merge(self, list1, list2): 
        merged = ListNode() 
        dummy = merged 
        while list1 and list2: 
            if list1.val <= list2.val: 
                dummy.next = list1
                list1 = list1.next 
            else: 
                dummy.next = list2 
                list2 = list2.next 
            dummy = dummy.next 

        if list1: 
            dummy.next = list1 
        if list2: 
            dummy.next = list2 

         
        return merged.next 
