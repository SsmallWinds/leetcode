'''
有序链表的k路合并

思路:
和两路合并类似，直接一一比较即可，时间复杂度时 O(nk)

优化，每次的一一比较可用最小堆优化，用最小堆得到最小值的时间复杂度时O(logk) 
所以优化后，时间复杂度为O(nlogk)

思路二:
两两合并
合并两个有序链表的复杂度为 O(logn)
两两合并则需合并logk次，总共的时间复杂度为 O(nlogk)

'''
from functools import total_ordering

@total_ordering
class LinkNode:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
    
    def __eq__(self, other):
        if self is None and other is not None:
            return False
        if self is not None and other is None:
            return False
        if self is None and other is None:
            return True
        return self.data == other.data

    def __le__(self, other):
        return self.data < other.data

def print_node(node:LinkNode)->None:
    res=[]
    while node!=None:
        res.append(node.data)
        node=node.next
    print(res)

def merge(nodes:list)->LinkNode:
    import sys
    res = LinkNode(-1)
    temp = res
    minimum = 0
    min_index = 0
    not_break = True
    cur=[node for node in nodes]
    while not_break:
        not_break = False
        minimum = sys.maxsize
        for i in range(len(nodes)):
            if cur[i] != None:
                # 有链表不为空则可继续循环
                not_break = True
                if cur[i].data < minimum:
                    min_index = i
                    minimum = cur[i].data
        if not not_break:
            break
        # 找到本次循环最小值后，移动对应链表的指针并追加到结果链表中
        temp.next = cur[min_index]
        temp = temp.next
        cur[min_index] = cur[min_index].next
    return res.next

def merge2(nodes:list)->LinkNode:
    import heapq

    pq = []
    cur = None
    res = LinkNode(-1)
    temp = res
    for node in nodes:
        heapq.heappush(pq, node)

    while len(pq) > 0:
        cur = heapq.heappop(pq)
        temp.next = cur
        temp = temp.next
        # pop出来的是最小值，所以如果当前节点的下一个节点不为空，
        # 加入最小堆即可进入下一轮循环
        if cur.next != None:
            heapq.heappush(pq, cur.next)
    return res.next

if __name__ == "__main__":
    a=LinkNode(2)
    a1=LinkNode(3)
    a2=LinkNode(4)
    a3=LinkNode(5)
    a4=LinkNode(6)
    a.next=a1
    a1.next=a2
    a2.next=a3
    a3.next=a4

    b=LinkNode(1)
    b1=LinkNode(7)
    b2=LinkNode(8)
    b3=LinkNode(9)
    b4=LinkNode(10)
    b.next=b1
    b1.next=b2
    b2.next=b3
    b3.next=b4

    c=LinkNode(9)
    c1=LinkNode(10)
    c2=LinkNode(100)
    c.next=c1
    c1.next=c2

    # print_node(merge([a, b, c]))

    print_node(merge2([a,b,c]))