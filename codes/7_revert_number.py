'''
目描述：给定一个范围为 32 位 int 的整数，将其颠倒。

例1：

输入：132

输出：321

例2：

输入：-123

输出：-321

例3：

输入：120

输出：21

注意：假设我们的环境只能处理 32 位 int 范围内的整数。根据这个假设，如果颠倒后的结果超过这个范围，则返回 0。
'''

def calc(input:int)->int:
    positive=input > 0
    input = input if positive else -input
    res = 0
    while input != 0:
        res = input % 10 + res * 10
        input = int(input / 10)
    return res if positive else -res

if __name__ == "__main__":
    input = -123
    print(calc(input))