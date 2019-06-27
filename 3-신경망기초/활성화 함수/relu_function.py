# -*- coding: utf-8 -*-
"""
ReLU 함수

좌표평면 상에서
0이하의 값은 0이고 0이상의 값에서는 x인 함수.
최근 신경망 분야에서 주로 사용된다고 한다. 
"""

import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 1)
y = relu(x)

plt.plot(x, y)
plt.ylim(-0.1, 4.1)
plt.show()
