# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        check = head.val
        itr = head.next
        result = ListNode(check)
        itr1 = result
        while itr:
            if check != itr.val:
                check = itr.val
                itr1.next = ListNode(check)
                itr1 = itr1.next
            itr = itr.next
        return result
        
