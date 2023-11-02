class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
#         row = "0"
        
#         while n > 0:
#             temp = ""
#             for d in row:
#                 if d == "0":
#                     temp += "01"
#                 else:
#                     temp += "10"
#             row = temp
#             n -= 1
        
#         s = 0
#         e = len(row)-1
        
#         while s <= e:
#             mid = (s+e)//2
#             if mid == k-1:
#                 return int(row[mid])
            
#             elif mid < k-1:
#                 s = mid + 1
            
#             elif mid > k-1:
#                 e = mid - 1


            current = 0
            left, right = 1, 2 ** (n - 1)

            for _ in range(n - 1):
                mid = (left + right) // 2
                if k <= mid:
                    right = mid
                else:
                    left = mid + 1
                    current = 0 if current else 1

            return current
            
            
            