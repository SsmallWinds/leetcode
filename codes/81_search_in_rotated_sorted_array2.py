"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

当重复的数字超过一半时，会出现nums[end] == nums[mid]的情况
当相等时，无法判断是左边有序还是右边有序
由于有nums[end] == nums[mid] 且 nums[mid] != target
所以nums[end] 一定不等于 target 所以可以直接 end --

时间复杂度分析
当重复项 = len(num - 1)时,退化成线性查找
最好O(logn) 最差O(n)
"""

def find(nums:list, target:int) -> bool:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = int((end + start) / 2)
        if nums[mid] == target:
            return True
        # 右边有序
        if nums[mid] < nums[end]:
            if target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        # 左边有序
        elif nums[mid] > nums[end]:
            if target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            end -= 1
    return False

if __name__ == "__main__":
    print(find([4,5,6,0,1,2,3], 3))
    print(find([1, 3, 1, 1, 1],3))

