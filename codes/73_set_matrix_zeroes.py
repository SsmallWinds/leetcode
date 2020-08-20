"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
"""

# m + n 的额外空间
def set_zero(m:list) -> None:
    row = set()
    col = set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                row.add(i)
                col.add(j)
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i in row or j in col:
                m[i][j] = 0

# 优化空间复杂度为常量，利用一个特殊值标记，再将特殊值替换为0
def set_zero2(m:list) -> None:
    MOD = -1
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                for row in range(len(m)):
                    if m[row][j] != 0:
                        m[row][j] = MOD
                for col in range(len(m[0])):
                    if m[i][col] != 0:
                        m[i][col] = MOD
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == MOD:
                m[i][j] = 0

def print_m(m:list) -> None:
    for line in m:
        print(line)
                
if __name__ == "__main__":
    m = [[0,1,2,0], 
        [3,0,5,2], 
        [1,3,1,5]]
    set_zero2(m)
    print_m(m)