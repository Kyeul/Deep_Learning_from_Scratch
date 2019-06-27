# -*- coding: utf-8 -*-
"""
numpy 모듈을 사용하지 않은 MSE(평균제곱오차) 만들기

"""
sum = 0
#배열 만들기
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0] #신경망 출력값(소프트 맥스 함수)
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] #정답 레이블

for i in range(len(y)):
    r = (y[i] - t[i])
    r= r*r
    sum = sum + r

result = sum / 2
print("정확도: "+ str(1-result))