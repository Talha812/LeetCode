class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #checking Rows Fully
        for i in range(len(board)):
            hold_dic = {}
            for j in range(len(board[i])):
                if board[i][j] in hold_dic and board[i][j] != ".":
                    return False
                else:
                    hold_dic[board[i][j]] = 1

                    
        #checking Columns Fully
        for i in range(len(board)):
            hold_dic = {}
            for j in range(len(board[i])):
                if board[j][i] in hold_dic and board[j][i] != ".":
                    return False
                else:
                    hold_dic[board[j][i]] = 1
                    
        
        def checking3x3matrix(array,start,end,colStart,colEnd):
            dic = {}
            for i in range(start,end):
                for j in range(colStart,colEnd):
                    if(array[i][j] in dic and array[i][j] != "."):
                        return False
                    else:
                        dic[array[i][j]] = 1   
            return True            
        
        matrix1 = checking3x3matrix(board,0,3,0,3)
        if(not matrix1):
            return False
        
        matrix2 = checking3x3matrix(board,0,3,3,6)
        if(not matrix2):
            return False
        
        matrix3 = checking3x3matrix(board,0,3,6,9)
        if(not matrix3):
            return False
        
        matrix4 = checking3x3matrix(board,3,6,0,3)
        if(not matrix4):
            return False
        
        matrix5 = checking3x3matrix(board,3,6,3,6)
        if(not matrix5):
            return False
        
        matrix6 = checking3x3matrix(board,3,6,6,9)
        if(not matrix6):
            return False
        
        matrix7 = checking3x3matrix(board,6,9,0,3)
        if(not matrix7):
            return False
        
        matrix8 = checking3x3matrix(board,6,9,3,6)
        if(not matrix8):
            return False
        
        matrix9 = checking3x3matrix(board,6,9,6,9)
        if(not matrix9):
            return False
        
        return True
        