# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:17:22 2021

@author: 李可豪
"""
from PIL import Image
import os

def file_name(file_dir):
    filename = []
    for root, dirs, files in os.walk(file_dir):
        filename.append(files)
    return filename

filenames = file_name('Wave_mel')

for file in filenames[0]:
    path = 'Wave_mel/'+file
    img = Image.open(path)   # 读取图片
    img = img.convert("L")   # 转化为黑白图片
    savepath = 'Wave_mel_black/'+file
    img.save(savepath)   # 存储图片
