# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        head2 = head
        while head:
            length += 1
            head = head.next
        mid = length // 2
        count = 0
        while head2:
            if count >= mid:
                return head2
            count += 1
            head2 = head2.next
            