class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        def reverse_String(arr, start, end):
            i = start
            j = end
            while(i < j):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
                j -= 1
            #print(arr)
            #return arr
        
        arr = []
        for ch in s:
            arr.append(ch)
        
        start = 0
        
        while(start < len(arr)):
            end = min(start+k-1,len(arr)-1)
            reverse_String(arr,start, end)
            start += 2*k
        
        return "".join(arr)
            