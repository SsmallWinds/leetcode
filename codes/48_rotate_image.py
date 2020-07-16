"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

思路：
先转置
再在横向翻转即可
"""


def transpose(raw: list) -> list:
    for i in range(len(raw)):
        for j in range(i):
            if i == j:
                continue
            temp = raw[i][j]
            raw[i][j] = raw[j][i]
            raw[j][i] = temp

    return raw


def turn(raw: list) -> list:
    row_size = len(raw[0])
    for k in range(len(raw)):
        for i in range(int(row_size / 2)):
            j = row_size - i - 1
            temp = raw[k][i]
            raw[k][i] = raw[k][j]
            raw[k][j] = temp
    return raw


def rotate(raw: list) -> list:
    transpose(raw)
    turn(raw)
    return raw


if __name__ == "__main__":
    raw = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    res = rotate(raw)
    for row in res:
        print(row)
