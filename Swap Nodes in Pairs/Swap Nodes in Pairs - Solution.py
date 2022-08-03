# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Some pointer stuff involved in this one.
        # 1. Init the dummy, its next is head. Initial previous is dummy, initial current is head.
        # 2. Set the nextPair, because we can't lose track of the rest of the list.
        # 3. Set the second node in the pair.

        # Init vars.
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        while current and current.next:
            nextPair = current.next.next
            second = current.next

            # At the start: CURRENT -> SECOND -> NEXT PAIR...
            # 4. Set second's next with current.
            # CURRENT -> SECOND -> CURRENT
            # 5. Set current's next with the pointer to the next pair, so we don't lose the rest of the list.
            # CURRENT -> NEXT PAIR...
            # 6. Set previous's next to second.
            # PREVIOUS -> SECOND -> CURRENT -> NEXT PAIR
            # Note how current and second are now flipped.
            second.next = current
            current.next = nextPair
            previous.next = second

            # Set previous and current so we can continue the statement loops.
            previous = current
            current = nextPair

        # Dummy next, not dummy.
        return dummy.next
