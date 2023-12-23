# Leetcode problem Dec 23
# Problem description:
# https://leetcode.com/problems/sort-list

# Preliminary version that sort of works, but with time limit exceeded
# for at least one of the submission test cases.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

       def _getNode(headNode: ListNode, numMoves: int) -> ListNode:
           nextNode = headNode
           for i in range(numMoves-1):
               nextNode = nextNode.next
           return nextNode

       
       def _searchInsert(sorted_length, headNode: ListNode, targetNode: ListNode) -> ListNode:
       
            targetVal = targetNode.val
            lastSortedNode = _getNode(headNode, sorted_length)

            if targetVal <= headNode.val:
                lastSortedNode.next = targetNode.next
                targetNode.next = headNode
                headNode = targetNode
                return headNode

            if targetVal >= lastSortedNode.val:
                return headNode

            low = 0
            high = sorted_length - 1
            midVal = 0
            while low <= high:
                mid = (low + high)//2
                midVal = _getNode(headNode, mid).val
                if targetVal > midVal:
                    low = mid + 1
                elif targetVal < midVal:
                    high = mid - 1
                else:
                    break

            
            
            if targetVal > midVal:
                prevNode = _getNode(headNode, mid)
            else:
                prevNode = _getNode(headNode, mid-1)

            # insert the target node
            lastSortedNode.next = targetNode.next
            targetNode.next = prevNode.next
            prevNode.next = targetNode

            return headNode

            
       headNode = head

       if not head:
           return None
      
       # sort the first 2 nodes
       if headNode.next:
           val1 = headNode.val
           val2 = headNode.next.val
           node2 = headNode.next
           if val2 < val1:   # swap positions
              headNode.next = node2.next
              node2.next = headNode
              headNode = node2
              print("Swap positions 1 and 2")
              print(f"Head node val: {headNode.val}")
              print(f"2nd node val: {headNode.next.val}")
       else:
            return headNode

       nextNode = headNode.next.next
       sorted_length = 2
       currNode = None
       while nextNode:
             currNode = nextNode
             nextNode = currNode.next
             headNode = _searchInsert(sorted_length, headNode, currNode)
             sorted_length += 1



       return headNode
    