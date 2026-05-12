# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            # prev = current
            # new = current.next
            # new.next = prev
            # current.next        
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev




            
             
        