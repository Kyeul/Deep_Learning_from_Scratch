# -*- coding: utf-8 -*-
"""
소프트맥스 함수 구현
softmax_function

소프트맥스 함수는
분자 = 입력신호의 지수함수
분모 = 모든 입력 신호의 지수함수의 합
으로 구성된다.

"""
#original softmax function
import numpy as np

def original_softmax(a):
    exp_a = np.exp(a) #신호 a의 지수함수
    sum_exp_a = np.sum(exp_a) # 신호 a들의 합
    y = exp_a / sum_exp_a 
    
    return y

#modified softmax function

"""
 원래의 소프트맥스 함수는 오버플로 문제가 발생할 수 있다.
 이를 방지하기 위해 변형한 소프트맥스 함수는 아래와 같다.
"""
 
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c) #오버플로 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
     
    return y
 