# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:11:06 2021

@author: 李可豪
"""
import os
import matplotlib
matplotlib.use('Agg') # No pictures displayed 
import pylab
import librosa
import librosa.display
import numpy as np


def file_name(file_dir):
    filename = []
    for root, dirs, files in os.walk(file_dir):
        filename.append(files)
    return filename

filenames = file_name('Data')
filenames = filenames[0]

for file in filenames:
    sig, fs = librosa.load('Data/'+file)   
    # make pictures name 
    save_path = 'Wave_mel/'+file[0:-4]+'.png'

    pylab.figure(figsize=(10, 4))
    pylab.axis('off') # no axis
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
    pylab.close()