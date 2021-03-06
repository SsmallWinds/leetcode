"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

任意两个皇后都不能处于同一行、同一列或同一斜线上
示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
 

提示：

皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。
当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。
当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）

思路：
很容易想到和数独类似，使用回溯法
"""


# 判断在row col 位置放置皇后的合法性
# 从上往下一行行的判断，所以不需要判断行的有效性和左下右下的有效性
def is_valid(queens: list, row: int, col: int) -> bool:
    # 列
    for line in queens:
        if line[col] == 'Q':
            return False

    # 左上
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if queens[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # 右上
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(queens):
        if queens[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True


def do_n_queens(queens: list, buf: list, row: int) -> None:
    import copy
    if len(queens) == row:
        buf.append(copy.deepcopy(queens))
        return

    for col in range(len(queens)):
        if not is_valid(queens, row, col):
            continue
        queens[row][col] = 'Q'
        do_n_queens(queens, buf, row + 1)
        queens[row][col] = '.'


def n_queens(n: int) -> list:
    queens = [['.' for _ in range(n)] for _ in range(n)]
    buf = []
    do_n_queens(queens, buf, 0)
    return buf


def print_queen(queens: list) -> None:
    print('-----------------------')
    for line in queens:
        print(line)
    print('-----------------------')


if __name__ == "__main__":
    res = n_queens(9)
    for i in res:
        print_queen(i)
    print('count:%d' % len(res))
