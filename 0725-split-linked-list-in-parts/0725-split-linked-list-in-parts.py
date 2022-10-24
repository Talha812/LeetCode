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
            
            for i in range(k):
                curr = head
                ans.append(curr)
                count = 1
                while(count < part_elements):
                    curr = curr.next
                    count += 1
                
                if(extra_elements>0):
                    curr = curr.next
                    extra_elements -= 1
                
                head = curr.next
                curr.next = None
            
            return ans
        
        