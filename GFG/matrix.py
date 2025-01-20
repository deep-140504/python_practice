# 1. Matrix Operations

class Solution:
    def endPoints(self, matrix, m, n):
        ##code here
        M = m
        N = n
        
        di = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}
        dir_0 = {"U": "R", "R": "D", "D": "L", "L": "U"}
        
        curr_dir = "R"
        i = 0
        j = 0
        while(i < m and j < n):
            ti, tj = i, j
            if(matrix[i][j] == 0):
                i = i + di[curr_dir][0]
                j = j + di[curr_dir][1]
                
            elif (matrix[i][j] == 1):
                matrix[i][j] = 0
                curr_dir = dir_0[curr_dir]
                i = i + di[curr_dir][0]
                j = j + di[curr_dir][1]
                
            if(i < 0 or i == m or j < 0 or j == n):
                return (ti, tj)
            
# 2. Last cell in a Matrix

class Solution:
    def endPoints(self, matrix, R, C):
        #code here
        m = R
        n = C
        di = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}
        dir_0 = {"U": "R", "R": "D", "D": "L", "L": "U"}
        
        curr_dir = "R"
        i = 0
        j = 0
        while(i < m and j < n):
            ti, tj = i, j
            if(matrix[i][j] == 0):
                i = i + di[curr_dir][0]
                j = j + di[curr_dir][1]
                
            elif (matrix[i][j] == 1):
                matrix[i][j] = 0
                curr_dir = dir_0[curr_dir]
                i = i + di[curr_dir][0]
                j = j + di[curr_dir][1]
                
            if(i < 0 or i == m or j < 0 or j == n):
                return (ti, tj)
            
#3. Assigning Subsequent Rows to Matrix first row elements

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]