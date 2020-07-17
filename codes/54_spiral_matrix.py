"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

思路，按照规则遍历，处理边界条件
维护四个边界值和前进方向
"""


def walk(raw: list) -> None:
    # 四个边界
    left = 0
    up = 0
    right = len(raw[0]) - 1
    down = len(raw) - 1
    # 遍历方向
    # 方向 0 右 1 下 2 左 3 上
    direction = 0
    # 当前位置
    row = 0
    col = 0

    while left <= col <= right and up <= row <= down:
        if direction == 0:
            for i in range(left, right + 1):
                print(raw[row][i])
            up += 1
            direction = 1
            col = right
            row = up
        elif direction == 1:
            for i in range(up, down + 1):
                print(raw[i][col])
            right -= 1
            direction = 2
            col = right
            row = down
        elif direction == 2:
            for i in range(right, left - 1, -1):
                print(raw[row][i])
            down -= 1
            direction = 3
            col = left
            row = down
        else:
            for i in range(down, up - 1, -1):
                print(raw[i][col])
            left += 1
            direction = 0
            col = left
            row = up


if __name__ == '__main__':
    raw = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]

    walk(raw)
