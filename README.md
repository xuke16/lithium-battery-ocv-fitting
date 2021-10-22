# lithium-battery-ocv-fitting
磷酸铁锂电池OCV-SOC曲线拟合python程序  
实现了两种拟合方法：1.多项式拟合；2.对数-多项式拟合  
使用方法：cmd 输入：python ocvFitting.py ocv文件路径 拟合方法  
如： python ocvFitting.py ocvdata.csv 多项式拟合  
 ![image](https://github.com/xuke16/lithium-battery-ocv-fitting/blob/master/Figure_1.png)
注意，excel里面是ocv数据，需要将第一列电压数据单独列到一个文件再运行脚本
