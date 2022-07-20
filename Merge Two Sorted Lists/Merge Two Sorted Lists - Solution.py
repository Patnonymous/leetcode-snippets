# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Init vars.
        dummy = ListNode()
        end = dummy

        # Loop through and compare. The pre-sorted lists make this simple.
        while list1 and list2:
            if list1.val < list2.val:
                end.next = list1
                list1 = list1.next
            else:
                end.next= list2
                list2 = list2.next
            # Remember to update the end.
            end = end.next

        # If one of the lists is empty...
        if list1:
            end.next = list1
        elif list2:
            end.next = list2

        # Do not return the original dummy node, use .next.
        return dummy.next