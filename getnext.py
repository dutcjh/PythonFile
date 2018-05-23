# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:10:47 2018

@author: dutch
"""

def get_next(s):
    
    prefix = [s[:i+1] for i in range(len(s)-1)]
    suffix = [s[i+1:] for i in range(len(s)-1)]
    l = list(set(prefix) & set(suffix))
    return l

        
if __name__ == "__main__":
    T = 'ababaaaba'
    print(get_next(T))