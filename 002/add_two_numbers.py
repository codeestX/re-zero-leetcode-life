# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = 1 if (l1.val + l2.val) >= 10 else 0
        head = ListNode((l1.val + l2.val) % 10)
        tail = head
        while l1.next is not None or l2.next is not None or temp == 1:
            l1 = l1.next if l1.next is not None else ListNode(0)
            l2 = l2.next if l2.next is not None else ListNode(0)
            node = ListNode((l1.val + l2.val + temp) % 10)
            temp = 1 if (l1.val + l2.val + temp) >= 10 else 0
            tail.next = node
            tail = node
        return head
