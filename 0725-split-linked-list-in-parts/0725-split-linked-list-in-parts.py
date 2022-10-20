# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        def getLength(head):
            curr = head
            count = 0
            while(curr):
                count += 1
                curr = curr.next
            return count
        
        ans = []
        N = getLength(head)
        if(k >= N):
            curr = head
            while(curr):
                record = curr
                dummy = record
                
                for i in range(1):
                    dummy = dummy.next
                    curr = curr.next
                    record.next = None
                    
                ans.append(record)
            
            if(k>N):
                for i in range(k-N):
                    ans.append(None)
            
            return ans
        
        else:
            remainder=N%k
            quotient=N//k
            temp=head
            for i in range(k):
                j=1
                if remainder>0:
                    length=quotient+1
                    remainder-=1
                else:
                    length=quotient
                x=temp
                ans.append(x)
                while j<=length:
                    x=temp
                    temp=temp.next
                    j+=1
                x.next=None

            return ans
#             part_elements = N//k
#             extra_elements = N%k

#             curr = head
            
#             while(curr):
#                 c = 1
#                 record = curr
#                 temp = record
#                 while(c != part_elements):
#                     node = ListNode(curr.next.val)
#                     temp.next(node)
#                     c += 1
#                     curr = curr.next
#                     temp = temp.next
                
#                 if(extra_elements > 0):
#                     temp.next(ListNode(curr.next.val))
#                     curr = curr.next
#                     extra_elements -= 1
#                     temp.next.next = None
                
#                 ans.append(record)


            return ans
        
        
        