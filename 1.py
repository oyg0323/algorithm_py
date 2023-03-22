import numpy as np
import matplotlib.pyplot as plt
x1 = np.arange(-0.1, 1.2, 0.1)
x2 = np.arange(-0.1, 1.2, 0.1)

def AND(x1, x2):
    x = np.array([x1, x2]) # 입력값
    w = np.array([0.4, 0.4]) # 가중치
    b = -0.7 # 편향
    tmp = np.sum(w*x) + b
    if tmp > 0:
        return 1
    else:
        return 0

def OR(x1, x2):
    if (x1 >0):
        t=1
    else:
        t=0
    if (x2 >0):
        k=1
    else:
        k=0
    x = np.array([t, k]) #입력값
    w = np.array([0.4, 0.4]) #가중치
    b = -0.2 #편향
    tmp = np.sum(w*x) + b
   # print(tmp)
    if tmp > 0:
        return 1
    else:
        return 0

def NAND(x1, x2):
    if (x1 > 0):
        t = 1
    else:
        t = 0
    if (x2 > 0):
        k = 1
    else:
        k = 0

    x = np.array([t, k]) #입력값
    w = np.array([-0.4, -0.4]) #가중치
    b = 0.7 #편향
    tmp = np.sum(w*x) + b

    if tmp > 0:
        return 1
    else:
        return 0

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

y = np.array([[XOR(_x1, _x2) for _x2 in x2] for _x1 in x1])

# 산점도 그리기
plt.scatter(x1[np.where(y==True)[0]], x2[np.where(y==True)[1]], marker='o', color='blue', label='True')
plt.scatter(x1[np.where(y==False)[0]], x2[np.where(y==False)[1]], marker='x', color='red', label='False')
plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)
plt.xticks(np.arange(-0.1, 1.2, step=0.1))
plt.yticks(np.arange(-0.1, 1.2, step=0.1))
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('XOR Gate')
plt.legend()

# 그래프 출력
plt.show()
