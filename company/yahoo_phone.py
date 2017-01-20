# /*
# The 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3
# 8 => 1000 => 1
# */
def binary(n):
    count =0
    while n >0:
        bit = n & 1
        if bit ==1:
            count +=1
        n = n>>1
    return count

# /*
# two strings are anagrams
# tar,rat
# */

def is_anagrams(s1,s2):

    if len(s1) != len(s2):
        return False

    count_dict ={}
    for c in s1:
        count_dict[c] = count_dict.get(c, 0)+1

    for c in s2:
        count = count_dict.get(c, 0)
        if count > 0:
            count_dict[c] = count -1
        else:
            return False
    return True



#  abbb , abb => False
#
#  /*
#  Given a 2-D array,
#  m x n matrix
#
# Given a integer matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 0  then make all the cells of ith row and jth column as 0.
#
# Without using any additional space
#
#  [1, 1, 0]
#  [2, 0, 1]
#  [1, 1, 1]
#
#
#  [0, 0, 0]
#  [0, 0, 0]
#  [1, 0, 0]
#
#  */
MAX = 2<<31 #Int.MAX +1

def convert(matrix):
     rows = len(matrix)
     cols = len(matrix[0])
     for row in range(rows):
         for col in range(cols):
             if matrix[row][col] == 0:
                set_col(matrix, rows, col, MAX)
                set_row(matrix, row, cols, MAX)

     for row in range(rows):
         for col in range(cols):
             if matrix[row][col] == MAX:
                 matrix[row][col] = 0


def set_col(matrix, rows, col, val):
    for row in range(rows):
        matrix[row][col] = val

def set_row(matrix, cols, row, val):
   for col in range(cols):
        matrix[row][col] = val

