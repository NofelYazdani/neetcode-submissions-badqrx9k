# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = newhead = ListNode()

        while head1 and head2:
            if head1.val > head2.val:
                newhead.next = head2
                head2 = head2.next
            else:
                newhead.next = head1
                head1 = head1.next
            newhead  = newhead.next
        if head1:
            newhead.next = head1
        elif head2:
            newhead.next = head2
        return dummy.next
             
        