"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

二分法
"""

def get_n(m:list, n:int) -> int:
    row = int(n / len(m[0]))
    col = n % len(m[0])
    return m[row][col]


def find_bin(m:list, target:int) -> bool:
    if len(m) == 0:
        return False
    if len(m[0]) == 0:
        return False
    size = len(m) * len(m[0])
    left = 0
    right = size - 1

    while left <= right:
        mid = int((left + right) / 2)
        cur = get_n(m, mid)
        if cur == target:
            return True
        if cur < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == "__main__":
    m = [[1,2,3,4], 
        [5,6,7,8], 
        [9,10,11,12]]

    print(find_bin(m, 8))


