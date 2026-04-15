class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # For rows
        for i in board:
            rows_unique = set()
            for j in i:
                if j == ".":
                    continue
                if j in rows_unique: 
                    return False
                rows_unique.add(j)
            
        # For columns
        l = 0
        while l < len(board[0]):
            cols_unique = set()
            for k in board:
                if k[l] == ".":
                    continue
                if k[l] in cols_unique:
                    return False
                cols_unique.add(k[l])
            l += 1
            
        # For boxes
        for row in range(0, 9, 3):
            for cols in range(0, 9, 3):
                box_unique = set()

                for i in range(row, row + 3):
                    for j in range(cols, cols + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in box_unique:
                            return False
                        box_unique.add(board[i][j])
            
        return True









        # # Check rows
        # for i in board:
        #     rows_unique.append(len(set(i)))
        # for i in unique_append:
        #     if i < 10:
        #         return false

        # #Check columns
        # for i in board:
        #     for j in i:
        #         columns_unique