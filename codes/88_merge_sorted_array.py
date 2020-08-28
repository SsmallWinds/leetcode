"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

"""

"""
思路就是归并排序的思路
为了做到空间复杂度为O(1)
需要复用原有空间
思路是归并前，将num1的元素都挪到数组的末尾即可
"""
def merge(nums1:list, nums2:list, m:int, n:int) -> list:
    for i in range(m-1,-1,-1):
        nums1[i + n] = nums1[i]
    k = 0
    i = 0
    j = 0
    print(nums1)
    print(nums2)
    while i < m or j < n:
        print(i, j, k)
        if i >= m:
            nums1[k] = nums2[j]
            j += 1
            k += 1
            continue
        if j >= n:
            nums1[k] = nums1[i + n]
            i += 1
            k += 1
            continue

        if nums1[i + n] <= nums2[j]:
            nums1[k] = nums1[i + n]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    return nums1


if __name__ == "__main__":
    nums1 = [1,2,0,0,0,0,0]
    m = 2
    nums2 = [0,5,6]
    n = 3
    print(merge(nums1, nums2, m, n))
