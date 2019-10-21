class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next=next
class myqueue():
    def __init__(self,max_num=10):
        self.max_num = max_num
        self.length=0
        self.left=None
        self.right=None
    def is_empty(self):
        return self.left==None  # 根据左侧节点判断队列是否为空
    def is_full(self):
        return self.max_num == self.length
    def enque(self,value):
        if not self.is_full():
            self.length+=1
            nd = Node(value)
            if self.is_empty():
                self.left=nd
                self.right=nd
            else:
                self.right.next=nd
                self.right=nd
        else:
            print('the queue is full ',value)
    def deque(self):
        if not self.is_empty():
            r = self.left
            self.left=self.left.next
            self.length-=1
            return r.data
        else:
            #raise ValueError('empty queue!')
            print('empty queue!')
    def to_list(self):
        if not self.is_empty():
            res_list = list()
            curr = self.left
            for i in range(self.length):
                res_list.append(curr.data)
                curr = curr.next
            return res_list

if __name__ == '__main__':
    q1 = myqueue(5)
    res = q1.to_list()
    print(res)
    print(q1.length)
    q1.enque(12)
    print(q1.length)
    q1.enque(23)
    print(q1.length)
    q1.enque(34)
    print(q1.length)
    q1.enque(45)
    print(q1.length)
    q1.enque(56)
    print(q1.length)
    res = q1.to_list()
    print(res)