# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Get center of the list
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the 2nd half of list
        pre, node = None, slow

        while node:
            pre, node.next, node = node, pre, node.next
            # next_node = node.next
            # node.next = pre
            # pre = node
            # node = next_node

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return

