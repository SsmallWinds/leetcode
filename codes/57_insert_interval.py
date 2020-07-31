"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

思路：
遍历列表
右边小于新节点左边的全部之间添加
继续遍历直到新节点右边小于左边，这个区间的节点合并为新节点
剩下的也之间添加
时间复杂度为O(n)
"""

def insert(raw:list, newNode:list) -> list:
    res = []
    i = 0
    while i < len(raw) and raw[i][1] < newNode[0]:
        res.append(raw[i])
        i+=1
    left = newNode[0]
    right = newNode[1]
    while i < len(raw) and raw[i][0] <= newNode[1]:
        left = min(newNode[0], raw[i][0])
        right = max(newNode[1], raw[i][1])
        i+=1
    res.append([left, right])
    
    while i < len(raw):
        res.append(raw[i])
        i+=1
    return res

if __name__ == "__main__":
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(insert([[1,3],[6,9]],[2,5]))
    