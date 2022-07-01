# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
                
        num = 1
        
        record_odd_indices_LL = odd_indices_LL = None
        record_even_indices_LL = even_indices_LL = None
        
        curr = head
        while(curr):
            temp = curr.next
            if(num % 2 != 0):
                if(odd_indices_LL == None):
                    odd_indices_LL = curr
                    record_odd_indices_LL = odd_indices_LL
                    odd_indices_LL.next = None
                else:
                    odd_indices_LL.next = curr
                    odd_indices_LL = odd_indices_LL.next
                    odd_indices_LL.next = None
            else:
                if(even_indices_LL == None):
                    even_indices_LL = curr
                    record_even_indices_LL = even_indices_LL
                    even_indices_LL.next = None
                else:
                    even_indices_LL.next = curr
                    even_indices_LL = even_indices_LL.next
                    even_indices_LL.next = None
            num += 1
            curr = temp
            
        if(record_odd_indices_LL == None):
            return record_even_indices_LL
        else:
            odd_indices_LL.next = record_even_indices_LL
        
        return record_odd_indices_LL