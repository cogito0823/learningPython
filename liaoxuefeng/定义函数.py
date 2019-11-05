#!/usr/bin/env pythhon
#-*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    for t in (a,b,c):    
        if not isinstance(t,(int,float)):
            raise TypeError('参数错误')
    delta = b*b-4*a*c
    if delta < 0:
        return '无解'
    elif delta == 0:
        x = (-b/(2*a),)
    else:
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        x = (x1,x2)
    return(x)

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
