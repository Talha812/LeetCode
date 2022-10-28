# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if (head == None or head.next == None):
            return head
    
        first = head
        sec = head
        temp = None
        
        i=1
        while(i<=k):
           
            temp = sec
            sec = sec.next
            
            i += 1
            
        while(sec):
            first = first.next
            sec = sec.next
        
        first.val, temp.val = temp.val,first.val
        
        return head
        """
        if(head == None):
            return head
        
        def getLength(head):
            curr = head
            count = 0
            while curr:
                count += 1
                curr = curr.next
            
            return count
        
        curr = head
        first_node = None
        sec_node = None
        
        first_count=1
        sec_count=1
        
        back_count = getLength(head) - k + 1
        while curr:
            if(first_count == k):
                first_node = curr
                
            if sec_count == back_count:
                sec_node = curr
            curr = curr.next
            first_count += 1
            sec_count += 1
        
        if first_node.next == sec_node.next:
            return head
        
        first_node.val, sec_node.val = sec_node.val, first_node.val
        
        # temp = first_node.val
        # first_node.val = sec_node.val
        # sec_node.val = temp
        
        return head
        """