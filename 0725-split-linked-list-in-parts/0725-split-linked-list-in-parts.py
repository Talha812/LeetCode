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
            part_elements=N//k
            extra_elements=N%k
            
            curr=head
            prev = None
            
            for i in range(k):
                count=1
                lenght = 0
                if extra_elements>0:
                    length = part_elements+1
                    extra_elements -= 1
                else:
                    length = part_elements
                
                ans.append(curr)
                    
                while count <= length:
                    prev = curr
                    curr = curr.next                        
                    count += 1
                
                if(prev):       
                    prev.next = None
                
                
            return ans

        