# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:22:01 2018

@author: dutch
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:08:40 2018

@author: dutch
"""

#链表节点结构实现  私有属性_pro_item是指向下个节点的指针，_item为此节点的值
class Node():
    def __init__(self,item = None,pos_item=None):
        self._item = item
        self._next = pos_item
        
    def __repr__(self):
        return str(self._item)

#单链表实现
class Chain():
    def __init__(self, item = None):
        if not item:
            self._head = None
            self.length = 0 
        elif isinstance(item,(list,tuple)):
            p = Node()
            self._head = p # 起始节点
            self.length = len(item) #长度
            for i in range(self.length):
                p._item = item[i]
                if i == self.length-1:
                    p._next = None
                else:
                    p._next = Node()
                    p = p._next
        else:
            self._head = None
            self.length = 0 
                        
    #判空
    def isEmpty(self):
        return self.length == 0

    # 索引
    def __getitem__(self, index):
        if self.isEmpty():
            print('This chain table is empty!')
            return
        if index < -self.length or index >= self.length:
            print("Error: index out of range")
            return 
        if index < 0:
            index += self.length
        count = 0
        node = self._head
        while True:
            if count == index:
                return node
            else:
                count += 1
                node = node._next

    #链表结尾插入
    def append(self,item):
        self.insert(-1, item)

    #插入数据
    def insert(self,index,item):
        if isinstance(item, Node):
            in_node = item
        else:
            in_node = Node(item)

        if index < -self.length-1 or index > self.length:
            print("error: index out of range")
            return
        if index < 0:
            index += self.length+1
        if index == 0: #加在最前
            in_node._next = self._head
            self._head = in_node
        elif index == self.length: #加在最后
            self[-1]._next = in_node
        else: # 加在中间
            in_node._next = self[index-1]._next
            self[index-1]._next = in_node
        self.length += 1


    #删除数据
    def delete(self,index):
        dnode = self[index]
        if dnode:
            if dnode == self._head:
                self._head = self._head._next
            else:
                self[index-1]._next = dnode._next
            self.length -= 1
        else: 
            return 
    def __len__(self):
        return self.length
    
    def clear(self):
        self._head = None
        self.length = 0 
        
    def __repr__(self):
        if self.isEmpty():
            print("the chain table is empty!")
            return "None"
        nlist = ""
        node = self._head
        while node:
            nlist += str(node._item) +' '
            node = node._next
        return nlist


if __name__ == '__main__':
    chain = Chain([])
    chain.append('A')
    chain.append('B')
    chain.append('C')
    chain.append('D')
    chain.append('E')
    chain.append('F')
    chain.append('G')
    print(chain)
    chain.insert(-1,'p')
    print(chain)
    chain.delete(7)
    print(chain,chain._head._item,chain.length)
    chain = Chain([1,2,3,4,5,6,7,8,9,10])
    print(chain, chain.length)