"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

思路:
将字符串分别排序，塞入map中，即为结果

"""


def get(raw: list) -> list:
    temp = {}
    for item in raw:
        key = ''.join(sorted(item))
        res = temp.get(key, None)
        if res is None:
            temp[key] = [item]
        else:
            res.append(item)
    return temp.values()


if __name__ == "__main__":
    print(get(["eat", "tea", "tan", "ate", "nat", "bat"]))
