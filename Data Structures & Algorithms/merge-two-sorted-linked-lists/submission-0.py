# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        f_head , s_head = list1, list2

        n_head = ListNode()
        ans = n_head
        while f_head and s_head:
            if f_head.val < s_head.val:
                n_head.next = f_head
                f_head = f_head.next
            else:
                n_head.next = s_head
                s_head = s_head.next
            
            n_head = n_head.next
        
        while f_head:
            n_head.next = f_head
            f_head = f_head.next
            n_head = n_head.next

        while s_head:
            print(s_head.val)
            n_head.next = s_head
            s_head = s_head.next
            n_head = n_head.next

    
        return ans.next
        