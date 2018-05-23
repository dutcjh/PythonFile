# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 09:57:11 2018

@author: dutch
"""
import string
import re
from mystack import Stack
import operator
# 定义运算的操作
operation = {'+':operator.add,'-':operator.sub,"/":operator.truediv,"*":operator.mul}
# 定义运算符的优先级
weight = {'(' : 100,'*' : 8,'/' : 8,'+' : 3,'-' : 3, None: 0}

# 判断一个字符串是否是数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

num1 = 0
num2 = 0
result = 0 
data_stack = Stack()  # 数字栈
oper_stack = Stack()  # 符号栈
def deal_data():
    p = oper_stack.pop() # 运算符出栈
    num2 = float(data_stack.pop()) # 数字2出栈
    num1 = float(data_stack.pop()) # 数字1出栈
    result = operation[p](num1, num2)
    print("%s %s %s 临时结果：%s" %(num1, p, num2, result))
    print("把计算的结果 %s 继续存入栈中" %result)
    data_stack.push(result)
    return result

while True:
    equation = input("请输入计算的式子(*提示英文状态下)：")
    # 对输入的算式字符串进行解析,eg:3*5，(99.8-52)*7+6-1.2*41
    #1.2-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
    while equation:
        cur = re.search(r'((^\d+\.?\d*)|(^\(\-\d+\.?\d*)|\(|\)|\+|\-|\*|/)',equation).group()
        print("---->",cur)
        if "(-" in cur:#考虑到负数的情形,如(-5.2)
            # 一分为二，"("与"-4"
            # 把左括号存入到符号栈中
            bracket=cur[0]
            print("----->",bracket)
            print("将%s存入到符号栈中"%bracket)
            oper_stack.push(bracket)
            equation=equation[1:]
            print("剩余的equation：",equation)

            # 把负数存入到符号栈中
            num=cur[1:]
            print("----->",num)
            print("将%s存入到数栈中"%num)
            data_stack.push(num)
            equation=equation[len(num):]
            print("剩余的equation：",equation)
        else:#非负情形
            lenth=len(cur)
            if is_number(cur):#数字则存入数栈
                print("将 %s 存入数栈data_stack"%cur)
                data_stack.push(cur)
            else:#非数字的符号
                if cur=="(":#左括号一律入栈
                    print("将%s存入到符号栈中"%cur)
                    oper_stack.push(cur)
                elif cur==")":#右括号则--将取两个数进行运算
                    deal_data()#处理数据的运算
                    #(12-5*8)再次判断“（”是否是符号栈的栈顶
                    while oper_stack.peek()!="(":
                        deal_data()
                    oper_stack.pop()#把左括号出栈

                else:#运算符
                    if oper_stack.peek()==None:#符号栈为空
                        print("将%s存入到符号栈中"%cur)
                        oper_stack.push(cur)
                    else:#符号栈不为空

                        if weight[cur]>weight[oper_stack.peek()]:#当前符号优先级“高于”栈顶元素的优先级
                            print("将%s存入到符号栈中"%cur)
                            oper_stack.push(cur)
                        else:#当前符号优先级“等于|低于”符号栈栈顶元素的优先级
                            if oper_stack.peek()=="(":
                                print("将%s存入到符号栈中"%cur)
                                oper_stack.push(cur)
                            else:
                                deal_data()
                                while weight[cur]==weight[oper_stack.peek()]:
                                    deal_data()
                                print("将%s存入到符号栈中"%cur)
                                oper_stack.push(cur)

            equation=equation[lenth:]
            print("剩余的equation：",equation)
    # 把算式逐个拆解完了，最后处理栈中还剩余的数据
    result=deal_data()
    while oper_stack.peek()!=None:
        result=deal_data()

    print("计算的结果为：\033[31;1m%s\033[0m" %result)
    break


