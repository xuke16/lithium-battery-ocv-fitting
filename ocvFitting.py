import matplotlib.pyplot as plt
import sys
import math
import pandas as pd
from scipy import optimize
from scipy import log
import matplotlib as mpl
from pylab import mpl
import sys
mpl.rcParams['font.sans-serif'] = ['SimHei']
# mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False
 
def ocv_soc(soc,a,b,c,d,e,f):
    y = a+b*soc+c*pow(soc,2)+d/(soc+0.00001)+e*log(soc+0.00001)+f*log(1+0.00001-soc)
    return y
 
def poly_ocvsoc(soc,k0,k1,k2,k3,k4,k5,k6,k7,k8,k9):
    y = k0+k1*soc+k2*pow(soc,2)+k3*pow(soc,3)+k4*pow(soc,4)+k5*pow(soc,5)+k6*pow(soc,6)+k7*pow(soc,7)+k8*pow(soc,8)+k9*pow(soc,9)
    return y
 
def main():
 
    path = sys.argv[1]
    path = path.replace("&"," ")
    Fit_method = sys.argv[2]
    if(Fit_method=="多项式拟合"):
        try:
            voltages = pd.read_table(path,header=None)
            voltages.columns = ['y']
            voltages.sort_values(ascending=False,by='y')
            voltages['x'] = list([1-(i-1)/voltages.shape[0] for i in range(1,voltages.shape[0]+1)])
            x = voltages['x'].tolist()[5:-5]
            y =voltages['y'].tolist()[5:-5]
        except:
            print('格式错误，请读取OCV列向量的文本文件，并且不小于10个点！')
            return
        k0, k1, k2, k3, k4, k5, k6, k7, k8, k9 = optimize.curve_fit(poly_ocvsoc,x,y,method='lm')[0]
        print(k0,k1,k2,k3,k4,k5,k6,k7,k8,k9)
        yy = [poly_ocvsoc(xx,k0,k1,k2,k3,k4,k5,k6,k7,k8,k9) for xx in x]
        print(poly_ocvsoc(1,k0,k1,k2,k3,k4,k5,k6,k7,k8,k9))
    else:
        try:
            voltages = pd.read_table(path, header=None)
            voltages.columns = ['y']
            voltages.sort_values(ascending=False, by='y')
            voltages['x'] = list([1 - (i - 1) / voltages.shape[0] for i in range(1, voltages.shape[0] + 1)])
            x = voltages['x'].tolist()[5:-5]
            y = voltages['y'].tolist()[5:-5]
        except:
            print('格式错误，请读取OCV列向量的文本文件，并且不小于10个点！')
            return
        a, b, c, d, e, f = optimize.curve_fit(ocv_soc, x, y, method='lm')[0]
        print("a=%f  b=%f  c=%f d=%f e=%f f=%f" %(a, b, c, d, e, f))
        yy = [ocv_soc(xx, a, b, c, d, e, f) for xx in x]
    f1 = plt.figure(1,figsize=(8,6))
    ax1 = plt.subplot(2,2,1)
    ax2 = plt.subplot(2,2,2)
    ax3 = plt.subplot(2,2,3)
    ax4 = plt.subplot(2,2,4)
    # f1.tight_layout()#调整整体空白
    #绘制原先的曲线
    plt.sca(ax1)
    plt.plot(x,y,'g:',label=u"原始数据")
    plt.xlabel('SOC',fontsize=14)
    plt.ylabel('OCV/V',fontsize=14)
    plt.tight_layout()
    # ax1.spines['top'].set_visible(False)
    # ax1.spines['right'].set_visible(False)
    # ax1.spines['bottom'].set_visible(False)
    # ax1.spines['left'].set_visible(False)
    plt.legend(fontsize=14)
    #绘制拟合的曲线
    plt.sca(ax2)
    plt.plot(x,yy,'b',label=u"拟合曲线")
    plt.xlabel('SOC',fontsize=14)
    plt.ylabel('OCV/V',fontsize=14)
    plt.tight_layout()
 
    plt.legend(fontsize=14)
    #拟合曲线对比
    plt.sca(ax3)
    plt.plot(x,y,'r--',label="原始曲线")
    plt.plot(x,yy,color='gray',label="拟合曲线")
    plt.xlabel('SOC',fontsize=14)
    plt.ylabel('OCV/V',fontsize=14)
    plt.tight_layout()
    plt.legend(fontsize=14)
    #拟合误差曲线
    plt.sca(ax4)
    error = [y1-y2 for y1,y2 in zip(y,yy)]
    plt.plot(x,error,color='r',label="误差曲线")
    plt.xlabel('SOC',fontsize=14)
    plt.ylabel('OCV/V',fontsize=14)
    plt.legend(fontsize=14)
    plt.tight_layout()
 
    plt.show()
main()
