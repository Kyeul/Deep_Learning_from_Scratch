# -*- coding: utf-8 -*-
"""
신경망에서의 행렬의 곱

넘파이 행렬을 사용해 신경망 구현
"""
import numpy as np
#import matplotlib.pylab as plt

#시그모이드 함수
def sigmoid(x):
    return 1 / (1+np.exp(-x))



X = np.array([1, 2])
print(X.shape)

W = np.array([[1, 3, 5], [2, 4, 6]])
print

Y = np.dot(X, W)
print(Y)

# 3층 신경망 구현하기

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape) #(2, 3)
print(X.shape) #(2,)
print(B1.shape) #(3,)

#활성화 함수 => 시그모이드 사용
# 1층 
A1 = np.dot(X, W1) + B1
Z1 =  sigmoid(A1)
print(A1)
print(Z1)

# 2층

W2 = np.array([
        [0.1, 0.4],
        [0.2, 0.5],
        [0.3, 0.6]
        ])
B2 = np.array([0.1, 0.2])

print(W2.shape) #(3, 2)
print(B2.shape) #(2,)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(A2)
print(Z2)

#3층 - 출력층
W3 = np.array([
        [0.1, 0.3],
        [0.2, 0.4]
        ])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
print(A3) #최종 출력 값
#출력층의 활성화 함수로 항등함수를 사용한다. 항등함수는 입력 값을 그대로 출력하는 함수다.
#따라서 따로 구현할 필요가 없기에 여기서는 사용하지 않았다.


