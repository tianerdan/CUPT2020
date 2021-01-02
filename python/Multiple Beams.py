# -*- coding: utf-8 -*-
'''
4.13.2 多光束干涉条纹的特点演示程序
拒绝内卷，从我做起！
Coder:Erdan TIAN@github.com/tianerdan
'''

import numpy as npy
import matplotlib.pyplot as plt

Rlist=[0.04,0.18,0.80]
for R in Rlist:
    F=4*R/(1-R)**2
    delta=npy.linspace(-1*npy.pi-2,3*npy.pi+2,5000)
    It0=1/(1+F*(npy.sin(delta/2))**2)# 表示It与I0的比值
    plt.plot(delta, It0, lw=2)
    plt.annotate("R=%.2f" % (R),(npy.pi*2.8,1/(1+F/2)))

plt.xlabel('$\delta$')
plt.ylabel('$I_{T}/I_{0}$',rotation=0)
plt.yticks(npy.linspace(0,1,6),["0","20%","40%","60%","80%","100%"])
plt.xticks([0,2*npy.pi],["2K$\pi$","(K+1)2$\pi$"])
plt.show()

'''
def format_func(value, tick_number):
    # 找到pi/2的倍数
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return '0'
    elif N == 1:
        return r'$\pi/2$'
    elif N == 2:
        return r'$\pi$'
    elif N % 2 > 0:
        return r'${0}\pi/2$'.format(N)
    else:
        return r'${0}\pi$'.format(N // 2)
 
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
这一块烂尾了。类里面嵌套plt翻车。
class Transmission(object):
    # 绘制多光束干涉透射光函数图像
    def __init__(self,R,x,l,n,h,i):
        # 标记同郭永康版光学4.13内容：
        # R=r^2表示反射率
        # x代表绘图自变量取值范围
        # l代表波长的\lambda
        # n代表介质折射率
        # h代表薄膜厚度
        # i代表入射角
        # ii代表在膜内的折射角i'
        self.ii=npy.arccos(npy.sin(i)/n)
        self.R,self.x,self.l,self.n,self.h,self.i=R,x,l,n,h,i
    def curves(self):
        F=4*self.R/(1-self.R)**2
        # delta = 4*npy.pi/self.l*self.n*self.h*npy.cos(self.ii)
        delta=npy.linspace(-2,2,800)
        It0=1/(1+F*(npy.sin(delta/2))**2)# 表示It与I0的比值
        line = plt.plot(delta, It0, lw=2)
        #plt.ylabel("I/I_{0}")
        #plt.xlabel("position (unit:mm)")
        print("Okay")
        return 0

x=2
l=632.8*1e-7
n=1.5
h=0.1
i=npy.pi/6
for R in [0.04,0.18,0.80]:
    Transmission(R,x,l,n,h,i)
plt.show()
'''