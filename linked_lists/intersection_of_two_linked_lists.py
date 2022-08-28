# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        top, bot = headA, headB

        # In the event they are different lengths, we want to
        # swap the heads so they meet in the middle at the
        # 2nd traversal
        while top != bot:
            top = headB if top is None else top.next
            bot = headA if bot is None else bot.next

        return top or bot

# Time Complexity: O(n + m) bc it only takes 2 traversals
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments
