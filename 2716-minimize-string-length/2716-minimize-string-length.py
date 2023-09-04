class Solution:
    def minimizedStringLength(self, s: str) -> int:
        
        arr = []
        for ch in s:
            arr.append(ch)
        
        
        for i in range(len(arr)):
            
            if arr[i] == -1:
                continue
            
            # Delete Left
            for j in range(i-1, -1, -1):
                if arr[j] == arr[i]:
                    arr[j] = -1
                    break
                    
            # Delete Right
            for j in range(i+1, len(arr)):
                if arr[j] == arr[i]:
                    arr[j] = -1
                    break
                    
        length = 0
        for val in arr:
            if val != -1:
                length += 1
        
        return length