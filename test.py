# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:08:40 2018

@author: dutch
"""

class Node:
    ''''' 链表节点实现 '''''
    def __init__(self, item = None, pos_item = None):
        self._item = item
        self._next = pos_item
    def __str__(self):
        return str(self._item)
    def __repr__(self):
        return str(self._item)

class Chain:
    ''''' 单链表实现 '''''
    def __init__(self):
        self._head = None
        self.length = 0
        
    # 判空
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
        
        
    # 链表结尾插入节点
    def append(self, item):
        if isinstance(item, Chain):
            node = item._head
        elif isinstance(item, Node):
            node = item
        else:
            node = Node(item)
        if self._head == None:
            self._head = node
        else:
            self[-1]._next = node
        self.length += getChainLen(node)
        
    
    def __add__(self, item):
        if isinstance(item, Chain):
            node = item._head
        elif isinstance(item, Node):
            node = item
        else:
            print('can only concatenate chain table to chain table')
            return self
        return self.append(node)
        
    # 插入节点
    def insert(self, index, item):          
        if isinstance(item, Chain):
            in_node = item._head
        elif isinstance(item, Node):
            in_node = item
        else:
            in_node = Node(item)
         
        if index == -1 or index == self.length:
            self.append(item)
            return 
        
        node = self[index]
        if node: # node不为空
            if node == self._head:
                self._head = in_node
                count = 1
                while True:
                    if in_node._next == None:
                        in_node._next = node
                        break
                    else:
                        in_node = in_node._next
                        count += 1
                self.length += count
            else:
                in_node_head = in_node
                count = 1
                while True:
                    if in_node._next == None:
                        in_node._next = node
                        break
                    else:
                        in_node = in_node._next
                        count += 1
                self[index-1]._next =  in_node_head       
                self.length += count
                
    # 删除数据
    def delete(self, index):
        dnode = self[index]
        if dnode:
            if dnode == self._head:
                self._head = self._head._next
                self.length -= 1
            else:
                self[index-1]._next = dnode._next
                self.length -= 1
        else:
            return 
                    
    def __repr__(self):
        if self.isEmpty():
            print('This chain table is empty!')
            return
        nlist = ""
        node = self._head
        for i in range(self.length):
            nlist += node._item + ' '
            node = node._next
            if node == None:
                break
        return nlist
            
def getChainLen(item):
    if isinstance(item, Node):
        count = 1
        while item._next:
            count += 1
            item = item._next
        return count
    elif isinstance(item, Chain):
        return item.length
    else:
        print('Is not a chain table!')
        return      
            
            

if __name__ == '__main__':
    chain = Chain()
    chain.append('A')
    chain.append('B')
    chain.append('C')
    chain.append('D')
    chain.append(Node('E',Node('F',Node('G'))))
    print(chain)
    anode = Node('1',Node('2',Node('3')))
    chain2 = Chain()
    chain2.append(anode)
    print(chain2)
    chain.append(chain2)
    print(chain)
    print(chain.length)
    
    chain.insert(1,chain2)
    print(chain)
    print(chain.length)
    chain.delete(0)
    print(chain,chain._head._item,chain.length)
    print(getChainLen(chain))
    
#        