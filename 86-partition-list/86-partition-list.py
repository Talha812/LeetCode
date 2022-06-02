# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
#         def printList(self, head):
#             curr = head
#             while curr is not None:   #(curr != None)  ===   while(curr)  ===     same
#                 print(curr.val, end=" -> ")
#                 curr = curr.next
    
#             print("\b\b\b")
    
        if(head == None):
            return head
    
        record_first = first_partition = None
        record_sec = sec_partition = None
        

        curr = head
        while(curr):
            temp = curr.next
            if(curr.val < x):
                if(first_partition == None):
                    first_partition = curr
                    first_partition.next = None
                    record_first = first_partition
                    
                else:
                    first_partition.next = curr
                    first_partition = first_partition.next
                    first_partition.next = None
                #printList(self, record_first)
            else:
                if(sec_partition == None):
                    sec_partition = curr
                    sec_partition.next = None
                    record_sec = sec_partition
                else:
                    sec_partition.next = curr
                    sec_partition = sec_partition.next
                    sec_partition.next = None
                #printList(self, record_sec)
                
            curr = temp
        if(first_partition == None):
            return record_sec
        else:
            first_partition.next = record_sec
            
        return record_first
        
                