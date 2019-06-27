import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(0, 6, 0.1)
#y1 = np.sin(x)
#y2 = np.cos(x)
#
#plt.plot(x, y1, label="sin")
#plt.plot(x, y2, linestyle="--", label="cos")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.title('sin & cos')
#plt.legend()
#plt.show()

#plt.plot(x, y)
#plt.show()

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
#
#print(AND(0, 0))
#print(AND(1, 0))
#print(AND(0, 1))
#print(AND(1, 1))

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) +b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0 
    else: return 1
   
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

#print(XOR(0, 0))
#print(XOR(1, 0))
#print(XOR(0, 1))
#print(XOR(1, 1))
#
#    

#print(NAND(0, 1))
#print(NAND(1, 0))
#print(NAND(0, 0))
#print(NAND(1, 1))
#
#print(OR(0, 1))
#print(OR(1, 0))
#print(OR(1, 1))
#print(OR(0, 0))
    
def step_function(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))


x= np.arange(-10.0, 10.0, 0.1)
y1 = step_function(x)
y = sigmoid(x)
plt.plot(x, y, label="sigmoid")
plt.plot(x, y1, linestyle="--", label="step")
plt.ylim(-0.1, 1.1)
plt.show()