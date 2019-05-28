# Given a binary grid i.e. a 2D grid only consisting of 0’s and 1’s, find the area of the largest rectangle inside the grid such that all the cells inside the chosen rectangle should have 1 in them. You are allowed to permutate the columns matrix i.e. you can arrange each of the column in any order in the final grid. Please follow the below example for more clarity.

# Lets say we are given a binary grid of 3 * 3 size.

# 1 0 1

# 0 1 0

# 1 0 0

# At present we can see that max rectangle satisfying the criteria mentioned in the problem is of 1 * 1 = 1 area i.e either of the 4 cells which contain 1 in it. Now since we are allowed to permutate the columns of the given matrix, we can take column 1 and column 3 and make them neighbours. One of the possible configuration of the grid can be:

# 1 1 0

# 0 0 1

# 1 0 0

# Now In this grid, first column is column 1, second column is column 3 and third column is column 2 from the original given grid. Now, we can see that if we calculate the max area rectangle, we get max area as 1 * 2 = 2 which is bigger than the earlier case. Hence 2 will be the answer in this case.
def solve(self, mat):
        R = len(mat)
        C = len(mat[0])
        if C==0:
            return 0
        hist = [[0 for i in range(C + 1)] for i in range(R + 1)] 
        for i in range(0, C, 1): 
              
            hist[0][i] = mat[0][i] 
            for j in range(1, R, 1): 
                if ((mat[j][i] == 0)): 
                    hist[j][i] = 0
                else: 
                    hist[j][i] = hist[j - 1][i] + 1

        for i in range(0, R, 1): 
            count = [0 for i in range(R + 1)] 
            for j in range(0, C, 1): 
                count[hist[i][j]] += 1
            col_no = 0
            j = R 
            while(j >= 0): 
                if (count[j] > 0): 
                    for k in range(0, count[j], 1): 
                        hist[i][col_no] = j 
                        col_no += 1
      
                j -= 1
        max_area = 0
        for i in range(0, R, 1): 
            for j in range(0, C, 1): 
                curr_area = (j + 1) * hist[i][j] 
                if (curr_area > max_area): 
                    max_area = curr_area 
      
        return max_area