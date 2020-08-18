"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

思路：
单纯的理解题意实现
"""
split = ' '

def get_blank(count:int) -> str:
     return ''.join([split for _ in range(count)])

def just(words:list, maxLen:int) -> list:
     cur = 0
     res = []
     start = 0
     end = 0
     i = 0
     while i < len(words):
          # 确定start 和 end, 间隙先假设为1个空格
          if cur == 0 or (cur + 1 + len(words[i])) <= maxLen:
               if cur == 0:
                    cur = len(words[i])
               else:
                    cur += (1 + len(words[i]))
               i += 1
               end += 1
          # 确定单行的单词为 start - end 区间内的单词，按规则补充空格
          else:
               # 计算间隙的空格数
               count = end - start - 1 
               sub = maxLen - cur + count
               # 只有一个词，直接补充空格
               if end - start == 1:
                    res.append(words[start] + get_blank(sub))
               else:
                    temp = ''
                    blank_count = int(sub / count)
                    miss = sub - blank_count * count
                    for j in range(miss):
                         temp += words[start + j] + get_blank(blank_count + 1)
                    for k in range(count - miss):
                         temp += words[start + miss + k] + get_blank(blank_count)
                    temp += words[end - 1]
                    res.append(temp)
               start = end
               cur = 0
     last = split.join([words[i] for i in range(start, end)])
     last += get_blank(maxLen - len(last))

     res.append(last)
     return res


if __name__ == "__main__":
     res = just(["Science","is","what","we","understand","well","enough","to","explain", \
          "to","a","computer.","Art","is","everything","else","we","do"], 20)
     res2 = just(["What","must","be","acknowledgment","shall","be"], 16)
     for line in res2:
          print(line)