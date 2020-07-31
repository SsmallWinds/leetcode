"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


"""

"""
将问题分解为子问题
即将集合分为n-1个已经合并好的和第n个区间
经第n个合并入已经合并好的区间即可
注意区分号不同情况的处理
时间复杂度为O(n ^ 2)
"""
def merge(raw:list) -> list:
    res = [raw[0]]
    for i in raw[1:]:
        left = None
        right = None
        toDel = []
        for j in res:
            # 左端点在的节点
            if j[0] <= i[0] <= j[1]:
                left = j
            # 右端点在的节点
            if j[0] <= i[1] <= j[1]:
                right = j
            # 新加入节点包含节点
            if i[0] < j[0] and i[1] > j[1]:
                toDel.append(j)

        for d in toDel:
            res.remove(d)

        # 左右都没找到节点，之间添加这个节点
        if left is None and right is None:
            res.append(i)
        # 左边没找到，右边找到了
        elif left is None and right is not None:
            res.append([i[0], right[1]])
        # 左边找到了右边没找到
        elif left is not None and right is None:
            res.append([left[0], i[1]])
        # 左右节点都找到了
        elif left is not None and right is not None:
            res.append([left[0], right[1]])

        # 删除被替换的节点
        if left is not None:
            res.remove(left)
        if right is not None:
            res.remove(right)
    return res
        

"""
源集合左端点排序
新加入的节点只需要和最后一个节点判断了
1> 新节点左节点大于最后一个节点右节点，则之间添加
2> 新节点左节点小于最后一个节点右节点，则最后一个节点右节点更新为较大的那个
时间复杂度为O(nlogn)
"""
def merge2(raw:list) -> list:
    raw.sort(key=lambda x: x[0])
    res = [raw[0]]
    for i in raw[1:]:
        if i[0] >  res[-1][1]:
            res.append(i)
        else:
            res[-1][1] = max(res[-1][1], i[1])
    return res

if __name__ == "__main__":
    data = [[1,4],[5,9],[3,6],[10,15]]
    print(merge2(data))