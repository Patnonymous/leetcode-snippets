# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Can be solved with two pointers.
        # For example with pointers p1 and p2, initialize p2 to an offset of n.
        # When p2 is null (None for Python), then p1 would be at the node we want to remove.

        # Init vars.
        # Allows us to remove the target at n, and handle
        # the n = 1 case.
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head

        # Offset the right.
        while n > 0 and right:
            right = right.next
            n -= 1

        # Traverse until right is None.
        while right:
            left = left.next
            right = right.next

        # Remove and return.
        left.next = left.next.next
        return dummyNode.next
