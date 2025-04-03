# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        
        slow , fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left, right):
        dummy = ListNode()
        itr = dummy

        while left and right:
            if left.val < right.val:
                itr.next = left
                left = left.next
            else:
                itr.next = right
                right = right.next
            itr = itr.next
        if left:
            itr.next = left
        if right:
            itr.next = right
        return dummy.next

        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not (head and head.next):
            return head
        left = head
        right = self.getMid(head)
        print(right.val)
        temp = right.next
        right.next = None
        right = temp
        left_half = self.sortList(left)
        right_half = self.sortList(right)

        return self.merge(left_half, right_half)