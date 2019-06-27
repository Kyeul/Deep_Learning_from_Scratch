# -*- coding: utf-8 -*-
"""
다차원 배열의 넘파이 계산 기초

"""

import numpy as np 

# 1차원 배열 A

A = np.array([1, 2, 3, 4])
print("== A ==")
print(np.ndim(A))  # 배열의 차원 수를 확인하는 함수
print(A.shape) # 배열의 형상 확인 원소의 개수를 알 수 있다. 단, tuple형태로 반환

# 2차원 배열 B
B = np.array([[1, 2], [3, 4], [5, 6]])
print("== B ==")
print(np.ndim(B))
print(B.shape) # 결과값인 (3, 2)는 처음 차원의 원소의 개수, 다음 차원의 원소의 개수를 뜻한다.

#행렬의 곲
print("== 행렬의 곲 ==")
#행렬의 계산은 왼쪽 행렬의 행과 오른 쪽 행렬의 열을 원소별로 곱하고 그 값들을 더한다.
A = np.array([[1, 2], [3, 4]])
print(A.shape)

B = np.array([[5, 6], [7, 8]])
print(B.shape)

C = np.array([1, 2])

print(np.dot(A, B)) # 행렬의 곱을 계산하는 함수. numpy.dot(행렬)
print(np.dot(B, A))
print(np.dot(C, A)) # 1차원 배열인 벡터와 행렬의 곱은 벡터가 된다. 

D = np.dot(A, B)
print(D.shape)

#행렬의 곱에서는 행렬의 형상에 주의 해야 한다.
# 구체적으로 이야기하면, 왼쪽 행렬의 1번 째 차원의 원소의 수와 오른 쪽 행렬의 0번째
# 차원의 원소의 수가 같아야 계산이 가능하다. 