#https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        #make two pointers - a slow one and a fast one
        slow = head
        fast = head.next
        
        while slow != fast:
            #if fast pointer reaches the end, the ll doesn't have a cycle
            if not fast or not fast.next:
                return False
            
            #increment slow by 1 and fast by two
            slow = slow.next
            fast = fast.next.next

        #if we reach a point where the slow and fast pointers converge,
        #the ll has a cycle
        return True