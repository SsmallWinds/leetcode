"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

 

示例 1：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
"""


"""
回溯法(深度优先遍历)
如果不考虑重复的情况
只需要同时遍历s1 s2 和 s3, 同时比较s1 和 s2 当前的位置是否和 s3相等，相等则后移
考虑到重复的情况
如果s1 s2 s3 当前遍历的位置字符相等，就需要尝试判断s1后移，如果无法得到最后结果
回溯尝试s2后移
"""
def check(s1:str, i:int, s2:str, j:int, s3:str, k:int) -> bool:
    # 长度不同一定不等
    if len(s1) + len(s2) != len(s3):
        return False

    # 都走到了尾部，返回True
    if len(s1) == i and len(s2) == j and len(s3) == k:
        return True

    # s1 到头， s2 和 s3 直接往后走
    if i == len(s1):
        while j < len(s2):
            if s2[j] != s3[k]:
                return False
            j += 1
            k += 1
        return True
    
    # s2 到头， s1 和 s3 直接往后走
    if j == len(s2):
        while i < len(s1):
            if s1[i] != s3[k]:
                return False
            i += 1
            k += 1
        return True

    # 如果当前的s1[i] == s3[k],继续往后走
    if s1[i] == s3[k]:
        if check(s1, i + 1, s2, j, s3, k + 1):
            return True
    
    # 如果当前的s2[j] == s3[k],继续往后走
    if s2[j] == s3[k]:
        if check(s1, i, s2, j + 1, s3, k + 1):
            return True

    return False

"""
动态规划：
令dp[i][j] 为s1 0-i 的子串 和 s2 0-j 的子串 是否满足 s3 0-i+j的子串
状态转换方程为:
如果 dp[i - 1][j] == True 且 s1[i - 1] == s3[i + j - 1] dp[i][j] = True
如果 dp[i][j - 1] == True 且 s2[j - 1] == s3[i + j - 1] dp[i][j] = True
否则 dp[i][j] == False
如果 i == 0 则判断 dp[i][j - 1] 且 s1[j - 1] == s3[j - 1] dp[i][j] = True
如果 j == 0 则判断 dp[i - 1][j] 且 s2[i - 1] == s3[i - 1] dp[i][j] = True

"""
def check2(s1:str, s2:str, s3:str):
    # 长度不同一定不等
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i - 1]
            else:
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or \
                                (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
    return dp[-1][-1]

"""
见图97_1 题目可以抽象成一个图,题解为是否有路径从左上角走到右下角
方法一是用的dfs遍历，那么也可以用bfs遍历
注意bfs的通用框架
利用一个队列和一个visited数组
将第一个元素塞进队列后, 将当前元素的下一个访问元素放入队列
进入下一次循环时，从队列中取出即可，放入队列时，可用visited数组记录元素是否访问过
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '%s,%s' % (self.x, self.y)
def check3(s1:str, s2:str, s3:str):
    # 长度不同一定不等
    if len(s1) + len(s2) != len(s3):
        return False
    visited = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    q = []
    q.append(Point(0, 0))

    while len(q) > 0:
        cur = q.pop()
        if cur.x == len(s1) and cur.y == len(s2):
            return True
        
        # 尝试向右走
        right = cur.x + 1
        if right <= len(s1) and s1[right - 1] == s3[right + cur.y - 1]:
            if not visited[right][cur.y]:
                visited[right][cur.y] = True
                q.append(Point(right, cur.y))

        # 尝试向下走
        down = cur.y + 1
        if down <= len(s2) and s2[down - 1] == s3[down + cur.x - 1]:
            if not visited[cur.x][down]:
                visited[cur.x][down] = True
                q.append(Point(cur.x, down))


    return False

if __name__ == "__main__":
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbcbcac'

    print(check(s1, 0, s2, 0, s3, 0))
    print(check2(s1, s2, s3))
    print(check3(s1, s2, s3))

