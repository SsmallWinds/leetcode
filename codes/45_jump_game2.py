"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的----最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。


贪心算法
每次都选择能到达的最大位置
"""


def jump(raw: list) -> int:
    end = 0
    max_pos = 0
    step = 0
    for i in range(len(raw) - 1):
        # 在这次能达到的范围内找能到达的最大值
        max_pos = max(max_pos, raw[i] + i)
        # 到达了这次的终点后
        # 最大值置为下一次跳跃的终点，同时步数加一
        if i == end:
            end = max_pos
            step += 1
    return step


if __name__ == "__main__":
    print(jump([2, 3, 1, 1, 4, 2, 1]))