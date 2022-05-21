# -*- coding: utf-8 -*-
"""
Created on Tue May  4 13:40:59 2021

@author: 李可豪
"""

#import
import pandas as pd
import wave
import pylab as pl
import numpy as np
from matplotlib.pyplot import savefig
from PIL import Image

import os
def file_name(file_dir):
    filename = []
    for root, dirs, files in os.walk(file_dir):
        filename.append(files)
    return filename

filenames = file_name('Data')

# 将wav文件转为波形图
for file in filenames[0]:
    path = 'Data/'+file
    f = wave.open(path, "rb")
    # 读取格式信息
    # (nchannels, sampwidth, framerate, nframes, comptype, compname)
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    # 读取波形数据
    str_data = f.readframes(nframes)
    f.close()
    #将波形数据转换为数组
    wave_data = np.fromstring(str_data, dtype=np.short)
    if len(wave_data) % 2 == 0:
        wave_data.shape = -1, 2
    else:
        wave_data = wave_data[0:len(wave_data)-1]
        wave_data.shape = -1, 2
    wave_data = wave_data.T
    
    time = np.arange(0, nframes) * (1.0 / framerate)
    len_time = int(len(time)/2)
    if len_time != wave_data.shape[1]:
        len_time = wave_data.shape[1]
    time = time[0:len_time]
    # 绘制波形
    pl.plot(time, wave_data[0])
    pl.xticks([])  #去掉横坐标值
    pl.yticks([])  #去掉纵坐标值
    savepath = 'Wave/'+file[0:-4]+'.png'
    savefig(savepath)
    pl.show()

#将图片名对应分类标签写入csv
filenames = filenames[0]
filenames = [filename[0:-3]+'png' for filename in filenames] 
emotion = [filename[7] for filename in filenames]
label = pd.concat([pd.DataFrame(filenames,columns=['filename']), 
                   pd.DataFrame(emotion,columns=['emotion'])],axis=1)
label.to_csv("label.csv",index=False,sep=',')
