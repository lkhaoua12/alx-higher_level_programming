#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    new_tuple_b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]
    
    a = new_tuple_a[0] + new_tuple_b[0]
    b = new_tuple_a[1] + new_tuple_b[1]
    return a, b

