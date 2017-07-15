# -*- coding:utf-8 -*-
import os
data={}
def dirlist(path):
    filelist =  os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            subfilelist =  os.listdir(filepath)
            subfile=[]
            for subfilename in subfilelist:
                subfile.append(subfilename)
            data[filename]=subfile



dirlist("./static/img")
print data
