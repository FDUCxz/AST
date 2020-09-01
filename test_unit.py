# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:49:51 2020

@author: CXZ
"""

from abstract_expression import AbstractExpression
from expression import SqlExpression
import pytest

def test_func1():
    interpreter = SqlExpression("Customer")
    input_sql = "(not(((a=name)and(b=id))or(c<=3)))"
    ast = interpreter.get_ast(input_sql)
    assert interpreter.get_sql(ast) == "(not(((a=name)and(b=id))or(c<=3)))"
    
    

def test_func2():
    interpreter = SqlExpression("Customer")
    input_sql = "(((a=name)and(b=id))or(c<=3))"
    ast = interpreter.get_ast(input_sql)
    assert interpreter.get_sql(ast) == "(((a=name)and(b=id))or(c<=3))"
    
def test_func3():
    interpreter = SqlExpression("Customer")
    input_sql = "(((a!=name)or(b=id))and(c<=3))"
    ast = interpreter.get_ast(input_sql)
    assert interpreter.get_sql(ast) == "(((a!=name)or(b=id))and(c<=3))"
    

    
    

if __name__ == "__main__":
    
    pytest.main(["test_unit.py"])
    
    

