y# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:11:15 2018

@author: 陈建辉
"""

from tkinter import *  
import time  

# MODE 0 秒表精确到百分秒  1 精确到十分秒  2 精确到1秒  3 精确到10秒
MODE = 3

class StopWatch(Frame):  
    '''''实现一个秒表部件'''  
    msec = 50  
    def __init__(self, parent=None, **kw):  
        Frame.__init__(self, parent, kw)  
        self._start = 45*60  
        self._elapsedtime = 0.0  
        self._running = False  
        self.timestr = StringVar()  
        self.makeWidgets()  
        self.flag  = True  
    def makeWidgets(self):  
        '''''制作时间标签'''  
        if MODE == 0 or MODE == 1:
            l = Label(self, font=("黑体", 30, "bold"), fg='blue', textvariable = self.timestr)  
        else:
            l = Label(self, font=("黑体", 40, "bold"), fg='blue', textvariable = self.timestr)  
        self._setTime(self._elapsedtime)  
        l.pack(fill = X, expand = NO, pady = 2, padx = 2)  
    def _update(self):  
        '''''更新时间'''
        self._elapsedtime = 45*60+9.9999 - (time.time() - self._start)
        self._setTime(self._elapsedtime)  
        self._timer = self.after(self.msec, self._update)  
    def _setTime(self, elap):  
        '''''将时间格式改为 分：秒：百分秒'''  
        minutes = int(elap/60)  
        seconds = int(elap-minutes*60.0)  
        if MODE == 0:
            hseconds = int((elap - minutes*60.0 - seconds) *100)  
            self.timestr.set('%02d:%02d:%02d' %(minutes, seconds, hseconds))  
        elif MODE == 1:
            tseconds = int((elap - minutes*60.0 - seconds) *10)  
            self.timestr.set('%02d:%02d:%01d0' %(minutes, seconds, tseconds))  
        elif MODE == 2:
            self.timestr.set('%02d:%02d' %(minutes, seconds))  
        else:
            self.timestr.set('%02d:%01d0' %(minutes, int(seconds/10)))  
    def Start(self):  
        if not self._running:  
            self._start = time.time() - self._elapsedtime  
            self._update()  
            self._running = True  
    def Stop(self):  
        '''''停止秒表'''  
        if self._running:  
            self.after_cancel(self._timer)  
            self._elapsedtime = time.time() - self._start  
            self._setTime(self._elapsedtime)  
            self._running = False  
    def Reset(self):  
        '''''重设秒表'''  
        self._start = time.time()  
        self._elapsedtime = 0.0  
        self._setTime(self._elapsedtime)  
    def stopwatch(self):  
        if self.flag == True:  
            self.pack(side = TOP)  
            Button(self, text = '开始', font=("黑体", 14, "bold"),  command = self.Start).pack(side = LEFT)  
            Button(self, text = '暂停', font=("黑体", 14, "bold"),  command = self.Stop).pack(side = LEFT)  
            Button(self, text = '重置', font=("黑体", 14, "bold"),  command = self.Reset).pack(side = LEFT)  
            # Button(self, text = '退出', font=("黑体", 24, "bold"),  command = self.destroy).pack(side = LEFT)       
        self.flag = False  

  
if __name__ == '__main__':  
    def main():  
        root = Tk()
        root.wm_attributes('-topmost',1)
        root.title("计时器 (ChenJianhui)")
        if MODE == 0 or MODE == 1:
            root.geometry('400x160')  
        else:
            root.geometry('200x100+10+10') 
        sw = StopWatch(root) # 创建一个实例
        sw.stopwatch()
        root.mainloop()  
    main()  
