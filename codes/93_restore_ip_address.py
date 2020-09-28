"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

 

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


思路：
回溯法
"""


def do_get_ips(nums:str, index:int, count:int, res:list, temp:str) -> None:
    # 剩余的长度不能大于 3*剩下的count
    if len(nums) - index > 3 * (4 - count):
        return

    # index到底了且正好添加了4个部分
    if index == len(nums):
        if count == 4:
            res.append(temp[:-1])
        return

    if index > len(nums) or count == 4:
        return

    # 添加一个数的情况
    do_get_ips(nums, index + 1, count + 1, res, temp + nums[index] + '.')

    # 只有一个数的情况能以0开头
    if nums[index] == '0':
        return

    # 添加两个数的情况
    if index + 2 <= len(nums):
        do_get_ips(nums, index + 2, count + 1, res, temp + nums[index:index + 2] + '.')

    # 添加三个数的情况，三个数需要判断<= 255
    if index + 3 <= len(nums) and int(nums[index:index + 3]) <= 255:
        do_get_ips(nums, index + 3, count + 1, res, temp + nums[index:index + 3] + '.')


def get_ips(nums:str) -> list:
    res = []
    do_get_ips(nums, 0, 0, res, "")
    print(res)


if __name__ == "__main__":
    s = "262255111"
    get_ips(s)