"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

思路:
首先直接考虑暴力法，将子串的可能的组合去分别匹配源字符串即可
"""


def is_swap(sz: list, start: int, end: int) -> bool:
    for i in range(start, end):
        if sz[i] == sz[end]:
            return False
    return True


def swap(sz: list, a: int, b: int) -> None:
    temp = sz[a]
    sz[a] = sz[b]
    sz[b] = temp


# 获取全排列
def perm(sz: list, start: int, end: int, res: list) -> None:
    import copy
    if start == end:
        res.append(copy.copy(sz))
    else:
        for i in range(start, end):
            # 判断是否可跳过本次递归
            # 当start到i之间有重复项，说明已经交换过了，需要跳过
            # eg. 1 2 3 3 在第一次递归时, i = 0,1,2 对应 1,2,3 开头, i = 3时, 3开头已经匹配过了
            if is_swap(sz, start, i):
                # 在本次递归固定住start之前的部分，
                # start之后的部分分别与start交换，移动start位置继续递归
                swap(sz, start, i)
                perm(sz, start + 1, end, res)
                swap(sz, start, i)


# 暴力法
def find_sub(sz: str, keys: list) -> list:
    res = []
    cases = []
    perm(keys, 0, len(keys), cases)
    cases = [''.join(item) for item in cases]
    ley_len = len(cases[0])
    for i in range(len(sz) - ley_len + 1):
        for case in cases:
            if sz[i:i + ley_len] == case:
                res.append(i)
                break
    return res


# 优化,判断i是否符合不需要生成全排列
# 思路是把key 放入一个map中
# 遍历i,由于每个key长度相同，所以只需要遍历i, i+len(key) ... i + len(key)*len(keys)是否在map中
# 不在则一定不符合，直接进入下一个循环
# 在的话，记录出现次数，出现次数 <= map中记录的key的数量则继续匹配如果 > map中记录的key的数量，也说明不匹配
def find_sub2(sz: str, keys: list) -> list:
    res = []
    map1 = {}
    for key in keys:
        exist = map1.get(key, None)
        if exist is None:
            map1[key] = 1
        else:
            map1[key] = exist + 1

    key_len = len(keys[0])

    for i in range(len(sz) - key_len + 1):
        map2 = {}
        count = 0
        while count < len(keys):
            word = sz[i + key_len * count:i + key_len * count + key_len]
            if word in map1:
                exist_count = map2.get(word, None)
                if exist_count is None:
                    exist_count = 1
                else:
                    exist_count += 1
                map2[word] = exist_count
                if exist_count > map1[word]:
                    break
                else:
                    count += 1
            else:
                break
            if count == len(keys):
                res.append(i)
    return res


if __name__ == '__main__':
    print(find_sub('barfoothefoobarman', ['foo', 'bar']))
    print(find_sub2('barfoofoothefoobarman', ['foo', 'bar']))
