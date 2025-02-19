# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp = dummy 
        while temp.next != None:
            while temp.next.val == val:
                temp.next = temp.next.next
                if temp.next == None:
                    break
            temp = temp.next
            if temp == None:
                break
        return dummy.next
        