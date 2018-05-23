# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 09:46:41 2018

@author: dutch
"""

#链表节点结构实现  私有属性_pro_item是指向下个节点的指针，_item为此节点的值
class Node():
    def __init__(self,item = None,pos_item=None):
        self._item = item
        self._next = pos_item
        
    def __repr__(self):
        return str(self._item)

class Stack():
    ''''' 链栈 '''''
    def __init__(self):
        self.top = None  # 初始化栈顶
        
    def peek(self):
        ''' 获取栈顶元素 '''
        if self.top != None:
            return self.top._item
        else:
            return None
    
    def push(self, n):
        ''' 入栈 '''
        n = Node(n) #实例化节点
        n._next = self.top
        self.top = n
        return n._item
    
    def pop(self):
        ''' 弹栈 '''
        if self.top == None:
            return None
        else:
            tmp = self.top._item
            self.top = self.top._next
            return tmp

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)   
    print(s.pop())
    print(s.pop())    
    print(s.pop())   
    
   