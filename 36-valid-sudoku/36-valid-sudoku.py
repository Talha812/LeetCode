class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #checking rows fully
        for i in range(9):
            nums = 0 # counting total numbers
            A = set()
            for j in range(9):
                if board[i][j] != ".":
                    A.add(board[i][j])
                    nums+=1
            if nums!=len(A):
                return False

        # checking columns fully
        for i in range(9):
            nums = 0 #counting total numbers
            A = set()
            for j in range(9):
                if board[j][i] != ".":
                    A.add(board[j][i])
                    nums+=1
            if nums!=len(A):
                return False
            

        def checking3x3matrix(array,start,end,colStart,colEnd):
            count = 0
            s = set()
            for i in range(start,end):
                for j in range(colStart,colEnd):
                    if(array[i][j] != "."):
                        s.add(array[i][j])
                        count += 1
                    if(len(s) != count):
                        return False
                        
            return True
        
        matrix1 = checking3x3matrix(board,0,3,0,3)
        #print("matrix1", matrix1)
        if(matrix1 == False):
            return False
        
        matrix2 = checking3x3matrix(board,0,3,3,6)
        #print("matrix2",matrix2)
        if(matrix2 == False):
            return False
        
        matrix3 = checking3x3matrix(board,0,3,6,9)
        #print("matrix3",matrix3)
        if(matrix3 == False):
            return False
        
        matrix4 = checking3x3matrix(board,3,6,0,3)
        #print("matrix4",matrix4)
        if(matrix4 == False):
            return False
        
        matrix5 = checking3x3matrix(board,3,6,3,6)
        #print("matrix5",matrix5)
        if(matrix5 == False):
            return False
        
        matrix6 = checking3x3matrix(board,3,6,6,9)
        #print("matrix6",matrix6)
        if(matrix6 == False):
            return False
        
        matrix7 = checking3x3matrix(board,6,9,0,3)
        #print("matrix7",matrix7)
        if(matrix7 == False):
            return False
        
        matrix8 = checking3x3matrix(board,6,9,3,6)
        #print("matrix8",matrix8)
        if(matrix8 == False):
            return False
        
        matrix9 = checking3x3matrix(board,6,9,6,9)
        #print("matrix9",matrix9)
        if(matrix9 == False):
            return False
        

        return True