class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        if ops == []:
            return m*n
        
        m_row = float("inf")
        m_col = float("inf")
        
        for op in ops:
            m_row = min(op[0], m_row)
            m_col = min(op[1], m_col)
        
        return m_row * m_col