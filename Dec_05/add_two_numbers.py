# Day 05 of Christmas Coding Challenge
# Problem statement:
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr = l1
        l2_ptr = l2
        carry = 0
        last_node = None
        node_list = []
        while l1_ptr or l2_ptr :
             l1_val = 0
             l2_val = 0
             if l1_ptr:
                 l1_val = l1_ptr.val
                 l1_ptr = l1_ptr.next
             if l2_ptr:
                 l2_val = l2_ptr.val
                 l2_ptr = l2_ptr.next
            
             sum = l1_val + l2_val + carry
             res = sum%10
             carry = sum//10

             # instantiate new node
             new_node = ListNode()
             new_node.val = res
             if last_node is not None:
                 last_node.next = new_node
             last_node = new_node
             node_list.append(new_node)

        if carry > 0:
            new_node = ListNode()
            new_node.val = carry
            last_node.next = new_node
            node_list.append(new_node)

        return node_list[0]
             
