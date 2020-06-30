'''
题目描述
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

思路:

使用查找表来解决该问题。

设置一个 map 容器 record 用来记录元素的值与索引，然后遍历数组 nums。

每次遍历时使用临时变量 complement 用来保存目标值与当前值的差值
在此次遍历中查找 record ，查看是否有与 complement 一致的值，如果查找成功则返回查找值的索引值与当前变量的值 i
如果未找到，则在 record 保存该元素与索引值 i
'''

def get_two_sum(nums:list, target:int)->list:
    res=[]
    temp={}
    for index in range(0,len(nums)):
        sub = target-nums[index]
        if nums[index] in temp:
            return [temp[nums[index]], index]
        else:
            temp[sub]=index
    return res

if __name__ == '__main__':
    nums=[2, 11, 7, 15, 100]
    target=9
    print(get_two_sum(nums, target))
