#-*-coding:utf-8 -*-
import os
import os.path
import codecs

rootdir = r"C:\Users\Razer\Documents\SURF\已整理\原文"
lines = 0

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        if filename.find('.txt') == -1:
            continue
        f = codecs.open(os.path.join(parent,filename), 'r', encoding="utf-8")
        lines += len(f.readlines())

print(lines)