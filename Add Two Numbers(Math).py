# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        if not l1 and not l2 and not c:
            return None

        total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
        node = ListNode(total % 10)
        node.next = self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            total // 10
        )
        return node
