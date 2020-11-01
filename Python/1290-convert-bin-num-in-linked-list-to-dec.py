# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # num = str(head.val)
        num = head.val
        while head.next:
            # num += str(head.next.val)
            # num = num * 2 + head.next.val
            num = num << 1 | head.next.val
            head = head.next
        # return int(num,2)
        return num
