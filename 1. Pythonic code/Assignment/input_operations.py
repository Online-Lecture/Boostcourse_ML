import itertools
from functools import reduce
import sys
import time

def insert_operation(length, input_num, input_oper):

    ops = {"0":(lambda x,y:x+y), "1":(lambda x,y: x-y), "2":(lambda x,y:x*y)}
    oper_permutation = []
    result = []
    list(oper_permutation.extend(
        [str(index)]*value) for index, value in enumerate(input_oper) if value > 0)
    permutation = [list(x) for x in set(itertools.permutations(oper_permutation))]
    for i in permutation:
        result.append(reduce(lambda x,y: ops[i.pop()](x,y), input_num))

    print(str(max(result))+"\n"+str(min(result)))
    
print(list(itertools.permutations('ABCD')))
    
        
