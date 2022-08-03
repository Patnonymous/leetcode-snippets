# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Consider this problem is an extension of Merge Sorted Lists.
        # Merge Sorted Lists code can be easily reused here.
        # This solution merges 2 LinkedLists then apends them to the merged list,
        # it continues while the index is in range.
        # Note the 2 in range() indicating this is stepping by 2.

        # Edge cases.
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            # Store merged, return later.
            merged = []

            # Start 0, stop at len(lists), step by 2.
            for index in range(0, len(lists), 2):
                list1 = lists[index]
                # There can be an odd number of lists.
                list2 = lists[index + 1] if (index + 1) < len(lists) else None

                merged.append(self.mergeLists(list1, list2))
            lists = merged
        return lists[0]

    # Merge list code from Leetcodes Q21 Merge sorted lists.
    # It is the same.

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        end = dummy

        while l1 and l2:
            if l1.val < l2.val:
                end.next = l1
                l1 = l1.next
            else:
                end.next = l2
                l2 = l2.next
            end = end.next
        if l1:
            end.next = l1
        if l2:
            end.next = l2
        return dummy.next
