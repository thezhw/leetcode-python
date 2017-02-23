# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from public.ListNode import ListNode


# 两次遍历
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 计算长度
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        # 删除
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(length - n):
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next


# 一次遍历
class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
head = node1

solution = Solution()
solution.removeNthFromEnd(head, 2)
