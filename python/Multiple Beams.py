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
