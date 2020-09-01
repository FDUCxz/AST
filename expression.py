# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:55:36 2020

@author: CXZ
"""

from abstract_expression import AbstractExpression

class SqlExpression(AbstractExpression):
    """
    具体的sql解释类，实现sql查询语句中相关联的解释操作。
    实现抽象表达式中所要求的接口，主要是一个get_expressions()方法和get_sql()方法。
    """
    
    def __init__(self, table):
        self.SYMBOLS = {'}': '{', ']': '[', ')': '('}
        self.SYMBOLS_L, self.SYMBOLS_R = self.SYMBOLS.values(), self.SYMBOLS.keys()
        self.table = table

    def get_ast(self, sql):
        """
        负责将输入的sql查询语句生成ast语法树，按照后序遍历的顺序存放在列表中 
        """
        ast = []
        left_index = []
        i = 0
        while i< len(sql):
            if sql[i] in self.SYMBOLS_L:
                left_index.append(i)
                i = i+1
            elif sql[i] in self.SYMBOLS_R:
                ast.append(sql[left_index[-1]:i+1])
                sql = sql.replace(sql[left_index[-1]:i+1], "")
                i = left_index[-1]
                left_index.pop(-1)
            else:
                i = i+1
        print("生成的语法树为：{}".format(ast))
        return ast
    
    def get_sql(self, ast):
        """
        负责解析语法树中的表达式和逻辑符，遍历输出、拼接成完整sql查询语句
        """
        and_or_marks = ["(and)","(or)"]
        not_mark = "(not)"
        sql = ""
        queue = []
        for i in ast:
            if i in and_or_marks:
                if len(queue) == 2:
                    sql = sql + "("+queue[0]+i[1:-1]+queue[-1]+")" 
                    queue = []                         
                elif len(queue) == 1:
                    sql = "("+sql+i[1:-1]+queue[-1]+")"
            elif i == not_mark:
                sql = "("+i[1:-1]+sql+")"
            else:
                queue.append(i)
        print("生成的sql语句为：select * from {} where {}".format(self.table, sql))
        return sql