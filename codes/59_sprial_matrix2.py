"""

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

思路：
和54题遍历旋转矩阵类似
改为遍历时赋值即可

"""

def gen_matrix(n:int) -> list:

    raw = [[-1 for _ in range(n)] for _ in range(n)]
    cur = 1

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
                raw[row][i] = cur
                cur += 1
            up += 1
            direction = 1
            col = right
            row = up
        elif direction == 1:
            for i in range(up, down + 1):
                raw[i][col] = cur
                cur += 1
            right -= 1
            direction = 2
            col = right
            row = down
        elif direction == 2:
            for i in range(right, left - 1, -1):
                raw[row][i] = cur
                cur += 1
            down -= 1
            direction = 3
            col = left
            row = down
        else:
            for i in range(down, up - 1, -1):
                raw[i][col] = cur
                cur += 1
            left += 1
            direction = 0
            col = left
            row = up
    return raw

if __name__ == "__main__":
    for line in gen_matrix(3):
        print(line)