"""
给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。

 
示例：

输入：S = "ADOBECODEBANC", T = "ABC"
输出："BANC"
 

提示：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

思路：双指针法
维护left right 两个指针，移动right直到子串满足要求
满足要求后，移动left，并判断当前子串是否最短，是则记录下left，right以及当前最短长度
移动left直到不满足要求后，再移动right，重复步骤直到right到右边界

判断是否符合要求可以利用hashmap

"""
def match(temp:dict) -> bool:
    for k, v in temp.items():
        if v > 0:
            return False
    return True

def substring(s:str, t:str) -> str:
    import sys
    left = -1
    right = -1
    min_len = sys.maxsize
    cur_left = 0
    cur_right = 0
    temp = {}
    for i in t:
        count = temp.get(i, 0)
        temp[i] = count + 1

    while cur_right < len(s):
        # 字符在字典中，计数减一
        if s[cur_right] in temp:
            temp[s[cur_right]] = temp[s[cur_right]] - 1
        # 判断个数全为0即表示覆盖了子串
        while match(temp):
            # 符合时，移动左指针，得到当前最小值
            cur_len = cur_right - cur_left
            if cur_len < min_len:
                left = cur_left
                right = cur_right
                min_len = cur_len
            # 在字典中说明移除的是t中的字符，计数加一
            if s[cur_left] in temp:
                temp[s[cur_left]] = temp[s[cur_left]] + 1
            # 移动左指针
            cur_left += 1
        # 移动右指针
        cur_right += 1

    if left == right == -1:
        return ''
    return s[left:right + 1]

if __name__ == "__main__":
    # substring("ADOBECODEBANC", "ABC")
    print(substring("a", "a"))
