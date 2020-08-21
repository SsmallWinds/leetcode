"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

深度优先搜索(DFS)

题目可以抽象为，矩阵中的任意一个点
沿着上下左右四个方向移动，能覆盖word的即为找到

DFS:
思路和回溯法基本相同
一般的套路是，维护一个visited的列表用于回溯时判断是否访问过

"""

def dfs(board:list, word:str, visited:list, row:int, col:int, index:int) -> bool:
    # 判断越界
    if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
        return False
    
    # 访问过或者当前访问节点和word当前位置不匹配
    if visited[row][col] or board[row][col] != word[index]:
        return False

    # 遍历完word了，说明匹配成功
    if index == len(word) - 1:
        return True

    # 增加访问过的标记
    visited[row][col] = True
    
    # 分别沿着上下左右方向查找
    up = dfs(board, word, visited, row - 1, col, index + 1)
    if up:
        return True
    down = dfs(board, word, visited, row + 1, col, index + 1)
    if down:
        return True
    left = dfs(board, word, visited, row, col - 1, index + 1)
    if left:
        return True
    right = dfs(board, word, visited, row, col + 1, index + 1)
    if right:
        return True

    # 上下左右都查找失败, 返回查找失败
    visited[row][col] = False
    return False

def check(board:list, word:str) -> bool:
    visited = [[False for _ in board[0]] for _ in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            # 以矩阵中的任意一个点作为开始，分别进行dfs
            if dfs(board, word, visited, i, j, 0):
                return True
    return False

if __name__ == "__main__":
    board = [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
            ]
    print(check(board, 'ASADEESE'))