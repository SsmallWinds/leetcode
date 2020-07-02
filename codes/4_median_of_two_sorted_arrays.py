'''
题目描述
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。 
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 你可以假设 nums1 和 nums2 不会同时为空。

示例1：
nums1 = [1, 3]
nums2 = [2]
    
则中位数是 2.0
    
示例2：
nums1 = [1, 2]
nums2 = [3, 4]
    
则中位数是 (2 + 3) / 2 = 2.5

题目解析:
输入:
数组a[5,7,9,11,13,15]
数组b[4,6,10,12,14]

中位数为10

数组a小于中位数部分分为a1 [5,7,9]; 大于中位数部分为a2 [11,13,15]
数组b同理分为b1 [4,6,10] b2 [12,14]

可以倒推中位数满足条件：
1.len(a1) + len(b1) = (len(a) + len(b)) / 2
2.所有的 a1和b1的值小于a2和b2中的值
3.中位数10是a1最后一位与者b1最后一位中的较大值

详解:
https://github.com/MisterBooo/LeetCodeAnimation/blob/master/0004-median-of-two-sorted-arrays/Article/0004-median-of-two-sorted-arrays.md
'''

def calc(a,b):
    if len(a) > len(b):
        a, b = b, a
    print(a)
    print(b)

    lena = len(a)
    lenb = len(b)

    leftn = int((lena + lenb + 1) / 2)

    start = 0
    end = lena

    res = -1

    # 开始对数组a进行二分找到符合上述三个条件的值
    # 设当前查找的数A = a[count1-1]
    # count2 = leftn - count1
    # 则对应的B = b[count2 - 1]
    # A左边的值和B左边的值(包括A, B) 一定小于等于 A右边的值和B右边的值
    while(start <= end):
        # 开始二分查找
        count1 = int((start + end) / 2)
        # (数组b <= 中位数的值的数量) = 总数量 - (数组a <= 中位数值的数量)
        count2 = leftn - count1
        # A 比 B的下一个数大，说明A 不可能符合条件并且 A的可能值只能是在A的左边，继续向左二分
        if count1 > 0 and a[count1 - 1]  > b[count2]:
            end = count1 - 1
        # B 比 A的下一个数大，说明A 不可能符合条件并且 A的可能值只能是在A的右边，继续向右二分
        elif count1 < lena and b[count2 - 1] > a[count1]:
            start = count1 + 1
        # 找到满足条件的值
        else:
            # 当a中所有数都在总数组的右边
            if count1 == 0:
                res = b[count2 - 1]
            # 当b中所有数都在总数组的右边
            elif count2 == 0:
                res = a[count1 - 1]
            else:
                res = max(a[count1 - 1], b[count2 - 1])
            # 总数为奇数
            if (lena + lenb) % 2 != 0:
                return res
            # 总数为偶数，则找到下一个数后相加除2
            else:
                next = 0
                # 当a中所有数都在总数组的左边
                if count1 == lena:
                    next = b[count2]
                # 当a中所有数都在总数组的左边
                elif count2 == lenb:
                    next = a[count1]
                else:
                    next = min(a[count1], b[count2])
                return (res + next) / 2

        print('start:%d, end:%d'%(start,end))
    return res

if __name__ == "__main__":
    a=[2,6,7,9,11,13,15]
    b=[3,4,5,8,10]

    print(calc(a, b))
    