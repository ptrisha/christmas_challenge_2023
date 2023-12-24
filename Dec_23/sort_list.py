# Leetcode problem Dec 23
# Problem description:
# https://leetcode.com/problems/sort-list

# This is my third version.  It passes all of the tests on Leetcode submission.
# This implementation is just mergesort, complexity is O(n log n).


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def getMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
            mid = head
            tail = head.next
            while tail:
                 tail = tail.next
                 if tail:
                     mid = mid.next
                     tail = tail.next
                
            return mid

        def mergeSubLists(head1: Optional[ListNode], head2: Optional[ListNode])->Optional[ListNode]:

            new_head = ListNode()
            tail = new_head
            list1 = head1
            list2 = head2
            while (list1) and (list2):
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next

            if list1:
                tail.next = list1
            elif list2:
                tail.next = list2

            return new_head.next

        if (head is None) or (head.next is None):
           return head

        # find the middle node in the linked list 
        mid = getMiddle(head)
        # split the list in 2 with mid node as the last node of the 1st list
        head1 = head
        head2 = mid.next
        mid.next = None

        sorted1_head = self.sortList( head1)
        sorted2_head = self.sortList( head2)

        sorted_head = mergeSubLists(sorted1_head, sorted2_head)

        return sorted_head
    