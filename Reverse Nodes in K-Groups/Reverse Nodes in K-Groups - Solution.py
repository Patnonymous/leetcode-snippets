# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Init vars.
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = self.getKNode(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next

            prev = kth.next
            current = prevGroup.next

            while current != nextGroup:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp

        # Return dummy next.
        return dummy.next

    # Return the Kth node.

    def getKNode(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current
