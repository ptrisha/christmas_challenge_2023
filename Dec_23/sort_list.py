# Leetcode problem Dec 23
# Problem description:
# https://leetcode.com/problems/sort-list

# This is the second version.  It passes 28 of the testcases, but
# encountered a TLE on a test in which the linked list contains 50000
# items in descending order from 50000 downto 1.
# For the next version, I will attempt a recursive algorithm such as
# merge sort.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def searchInsert(nums: List[int], target: int) -> int:
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high)//2
                if target > nums[mid]:
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    return mid

            if target > nums[mid]:
                return mid+1
            else:
                if mid > 0:
                    return mid
                else:
                    return 0
        

        if head is None:
            return None

        if head.next is None:
            return head

        # keep a list of the last node of subsequence with the same node val
        lastNodeList = [head]
        valList = [head.val]

        headNode = head
        nextNode = head.next
        while nextNode:
            currNode = nextNode
            nextNode = currNode.next
            currVal = currNode.val
            if currVal in valList:
                valIndx = valList.index(currVal)
                lastNodeSameVal = lastNodeList[valIndx]
                currNode.next = lastNodeSameVal.next
                lastNodeSameVal.next = currNode
                lastNodeList[valIndx] = currNode
            else:   # search and insert 
                if (currVal-1) in valList:
                    pos = valList.index(currVal-1) + 1
                elif (currVal+1) in valList:
                    pos = valList.index(currVal+1)
                else:
                    pos = searchInsert(valList, currVal)
                    
                #print(f"Pos for inserting currVal:{currVal} is {pos}")
                # insert the new val in valList
                valList.insert(pos, currVal)
                # insert the node
                lastNodeList.insert(pos, currNode)
                # adjust adjacent pointers

                if pos == 0:
                    currNode.next = headNode
                    headNode = currNode
                    lastNodeList[-1].next = None
                elif pos == len(valList) - 1:
                    lastNodeList[pos-1].next = currNode
                    currNode.next = None
                else:
                    currNode.next = lastNodeList[pos-1].next
                    lastNodeList[pos-1].next = currNode


        return headNode
    

