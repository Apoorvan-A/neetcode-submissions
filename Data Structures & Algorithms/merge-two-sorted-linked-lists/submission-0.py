# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        temp=res
        ptr1=list1
        ptr2=list2

        while ptr2 and ptr1:
            if(ptr1.val<=ptr2.val):
                temp.next=ptr1
                temp=temp.next
                ptr1=ptr1.next
            else:
                temp.next=ptr2
                temp=temp.next
                ptr2=ptr2.next

        while ptr1:
            temp.next=ptr1
            temp=temp.next
            ptr1=ptr1.next
        while ptr2:
            temp.next=ptr2
            temp=temp.next
            ptr2=ptr2.next
        return res.next
            
