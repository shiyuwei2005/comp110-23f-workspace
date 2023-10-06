"""EX04 - `list` Utility Functions"""
__author__ = "730674854"
from random import randint

int1: int = randint(0,100)
int2: int = randint(0,100)
int3: int = randint(0,100)
list_: list[int] = [int1,int2,int3]

def all(list_int: list[int], int_choice: int) -> bool:
    index: int = 0
    while index <= len(list_int)-1:
        if list_int[index] != int_choice:
            return False
        index += 1 
    return True 


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    attempt: int = 0
    max_int: int = input[attempt]
    while attempt <= len(input)-1:
        if max_int < input[attempt]:
            max_int = input[attempt]
        attempt += 1
    return max_int 

def is_equal(list1: list[int], list2: list[int])-> bool:
    if len(list1) != len(list2):
        return False
    count: int = 0 
    while count <= len(list1)-1:
        if list1[count] != list2[count]:
            return False
        count += 1 
    return True 

    



    
        





