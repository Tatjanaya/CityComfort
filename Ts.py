#coding=utf-8
import epsilon2GZ_gui
import argparse
import numpy as np
import get_wv
import itertools
import math


parser = argparse.ArgumentParser()

parser.add_argument("--savedir",default="saved_models")

parser.add_argument("--outdir",default="out2")
args = parser.parse_args()

# 调用方式为 Ts = Ts_cal(f10,f11,f4,f5,fc)
# f10,f11,f4,f5,fc 分别是10,11,4,5波段和地表分类数据位置

def Ts_cal(f10,f11,f4,f5,fc):
    T10,T11,wv=get_wv.get_wv(f10,f11)
    rows, cols = T10.shape
    ts = np.zeros((rows,cols))
    epsilon1,epsilon2 = epsilon2GZ_gui.fun_epsilon(f10,f11,f4,f5,fc)
    c0=-0.268
    c1=1.378
    c2=0.183
    c3=54.30
    c4=-2.238
    c5=-129.20
    c6=16.40
    r=0.984
    I_hc = np.zeros((rows, cols))
    ts=T10+c1*(T10-T11)+c2*(T10-T11)*(T10-T11)+c0+(c3+c4*wv)*(1-((epsilon1+epsilon2)/2))+(c5+c6*wv)*(epsilon1-epsilon2) #地表温度
    wv = np.log((wv + 0.1107) / 0.2103 / 0.6108) * (237.3 + ts - 273.15) / (17.27 * (ts - 273.15)) 
    itertools.product(range(0,rows),range(0,cols))
    for item in itertools.product(range(0,rows),range(0,cols)):
        i=item[0]
        j=item[1]
        #aep=(epsilon1[i][j]+epsilon2[i][j])/2
        #dep=epsilon1[i][j]-epsilon2[i][j]
        
        #wv[i][j] = math.log((wv[i][j] + 0.1107) / 0.2103 / 0.6108) * (237.3 + ts[i][j] - 274.15) / (17.27 * (ts[i][j] - 274.15))  
        # 转相对湿度
        if (ts[i][j] - 274.15) < 5:
            wv[i][j] = wv[i][j] / 6.79
        elif (ts[i][j] - 274.15) < 10:
            wv[i][j] = wv[i][j] / 9.39
        elif (ts[i][j] - 274.15) < 15:
            wv[i][j] = wv[i][j] / 12.82
        elif (ts[i][j] - 274.15) < 20:
            wv[i][j] = wv[i][j] / 17.27
        elif (ts[i][j] - 274.15) < 25:
            wv[i][j] = wv[i][j] / 23.01
        elif (ts[i][j] - 274.15) < 30:
            wv[i][j] = wv[i][j] / 30.31
        else:
            wv[i][j] = wv[i][j] / 39.51
    I_hc = ts-274.15-0.55*(1-wv)*(ts-274.15-14.4)  
    print("end LST")
    np.savetxt("./datas/result.txt",I_hc, fmt='%f', delimiter=' ') #写txt
    return ts,I_hc


