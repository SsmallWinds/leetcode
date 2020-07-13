"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


上图是一个部分填充的有效的数独。

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1:

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true
示例 2:

输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
说明:

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。

思路：
根据条件，分别检查行，列，3*3的方块

"""


def check_row(raw: list) -> bool:
    temp = {}
    for i in raw:
        if i != '.':
            if i in temp:
                return False
            else:
                temp[i] = 1
    return True


def check_col(raw: list, col: int) -> bool:
    temp = {}
    for i in raw:
        if i[col] != '.':
            if i[col] in temp:
                return False
            else:
                temp[i[col]] = 1
    return True


def check_small(raw: list, col: int, row: int) -> bool:
    temp = {}
    for i in range(3):
        for j in range(3):
            cur = raw[3 * col + i][3 * row + j]
            if cur != '.':
                if cur in temp:
                    return False
                else:
                    temp[cur] = 1
    return True


def valid(raw: list) -> bool:
    for i in range(9):
        if not check_row(raw[i]):
            return False

    for i in range(9):
        if not check_col(raw, i):
            return False

    for i in range(3):
        for j in range(3):
            if not check_small(raw, i, j):
                return False

    return True


# 将行中的值表示为(row)x 列中的值表示为 x(col) 小方块中的值表示为 (row)(col)x
# 再利用hash,只需要遍历一次
# 参考 https://leetcode.wang/leetCode-36-Valid-Sudoku.html 很巧妙
def valid2(raw: list) -> bool:
    temp = {}

    for i in range(9):
        for j in range(9):
            if raw[i][j] != '.':
                keys = ['(%d)%s' % (i, raw[i][j]),
                        '%s(%d)' % (raw[i][j], j),
                        '(%d)(%d)%s' % (int(i/3), int(j/3), raw[i][j])]
                for key in keys:
                    if key in temp:
                        return False
                    else:
                        temp[key] = 1
    return True


if __name__ == "__main__":
    raw = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

    print(valid(raw))
    print(valid2(raw))
