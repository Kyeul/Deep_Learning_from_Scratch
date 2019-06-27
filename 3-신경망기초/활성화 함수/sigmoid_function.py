# -*- coding: utf-8 -*-
"""
시그모이드 함수 

시그모이드 함수는 계단 함수와 달리 0과 1사이의 값이 연속적으로 변한다.
'시그모이드'란 S자 모양이란 뜻으로, 그래프를 보면 그 의미를 직관적으로 알 수 있다.
"""

import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1+np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

