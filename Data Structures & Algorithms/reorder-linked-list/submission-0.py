# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#               BRUTE FORCE SOLUTION
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []
        current = head
        while current:
            array.append(current)
            current = current.next


        i = 0
        j = len(array) - 1
        
        while i < j:
            array[i].next = array[j]

            i += 1
            if i == j:
                break
            array[j].next = array[i]            
            j -= 1

        array[i].next = None
        
        
        


        