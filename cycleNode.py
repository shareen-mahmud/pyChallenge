# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        else:
            slow = head
            list1 = []
            while slow is not None:
                if slow not in list1:
                    list1.append(slow)
                    slow = slow.next
                else:
                    return slow
