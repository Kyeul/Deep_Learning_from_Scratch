# -*- coding: utf-8 -*-
"""
교차엔트로피 오차

평균 제곱오차에 비해 계산 속도가 월등히 빠르다.
"""
import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7
    return - np.sum(t* np.log(y + delta))

