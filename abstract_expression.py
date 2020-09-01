# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:52:03 2020

@author: CXZ
"""

from abc import ABCMeta, abstractmethod
 
class AbstractExpression():
    """
    抽象表达式类，声明一个抽象的解释操作，这个接口为抽象语法树中所有的节点所共享
    """
    __metaclass__ = ABCMeta
     
    @abstractmethod
    def interpret(self, context):
        pass 
    
    

