# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reversed order allows us to just add: Ones digit, tens digit, hundreds digit, ... so on.

        # Init dummy node and current.
        dummyNode = ListNode()
        current = dummyNode

        carryValue = 0
        # Loop while lists exist, or the carry exists.
        while l1 or l2 or carryValue:
            # Remember to account for the None's.
            valueOne = l1.val if l1 else 0
            valueTwo = l2.val if l2 else 0

            # Calculate the new digit.
            newValue = valueOne + valueTwo + carryValue
            # Extract the carry value from the result.
            carryValue = newValue // 10
            # Extract the result value.
            newValue = newValue % 10
            # Set next.
            current.next = ListNode(newValue)

            # Set vars.
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # Return result.
        return dummyNode.next
