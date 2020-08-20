"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""

def sort_color(colors:list) -> None:
    red = 0
    write = 0
    blue = 0
    for i in colors:
        if i == 0:
            red += 1
        elif i == 1:
            write += 1
        else:
            blue += 1
    index = 0
    for i in range(red):
        colors[i] = 0
    
    for i in range(write):
        colors[i + red] = 1

    for i in range(blue):
        colors[i + red + write] = 2

def swap(colors:list, n:int, m:int) -> None:
    temp = colors[n]
    colors[n] = colors[m]
    colors[m] = temp

# 维护两个指针 n0 和 n2, n0 左边的是 0， n2右边的是2,
def sort_color2(colors:list) -> None:
    n0 = 0
    n2 = len(colors) - 1
    i = 0
    while i <= n2: 
        if colors[i] == 0:
            swap(colors, i, n0)
            n0 += 1
        elif colors[i] == 2:
            swap(colors, i, n2)
            n2 -= 1
            # 从n2 位置换过来的需要重新判断一次，故i--，下次循环再次判断i位置上的值
            i -= 1
        i += 1

if __name__ == "__main__":
    colors = [2,1,2]
    sort_color2(colors)
    print(colors)