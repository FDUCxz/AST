# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:11:23 2020

@author: CXZ
"""

from abstract_expression import AbstractExpression
from expression import SqlExpression


if __name__ == "__main__":
    interpreter = SqlExpression("Customer")
    input_sql = "(not(((a=name)and(b=id))or(c<=3)))"
    ast = interpreter.get_ast(input_sql)
    interpreter.get_sql(ast)
    
    