# This code checks a linked list for cycles.
# It uses the Floyd algorithm for detecting cycles.
# This algorithm makes use of two pointers: slow pointer
# which traverses the list a node at a time while
# the fast pointer traverses 2 nodes at once.  If the
# pointers meet, that is when a cycle is detected.
#
# Description of the problem on Leetcode:
# https://leetcode.com/problems/linked-list-cycle/
# The description is horrible, btw.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if (pos == -1) or (head is None):
           return False

        slow_p = head
        fast_p = head
        while (slow_p and fast_p and fast_p.next):
               slow_p = slow_p.next
               fast_p = fast_p.next.next
               if slow_p == fast_p:
                   return True
            
        return False
    