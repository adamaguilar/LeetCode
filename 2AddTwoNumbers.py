'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = l3 = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry = carry + l1.val
                l1 = l1.next
            if l2:
                carry = carry + l2.val
                l2 = l2.next
            l3.val = carry % 10
            carry = carry // 10
            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
        return result

l1, l1.next, l1.next.next = ListNode(2), ListNode(4), ListNode(3)
l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)
result = Solution().addTwoNumbers(l1, l2)
print([result.val, result.next.val, result.next.next.val])