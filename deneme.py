# -*- coding: utf-8 -*-
#Bu kod txt_path yolundaki txt dosyalarında 7 olan label id'leri 0'a cevirip output dosyasında 
#txt dosyalarını oluşturuyor

from os import listdir
from os.path import isfile, join

output_path = r"C:\Users\fatmadelenn\Desktop\python\output"
txt_path = r"C:\Users\fatmadelenn\Desktop\python\txt_path"
onlyfiles = [f for f in listdir(txt_path) if isfile(join(txt_path, f))]

for file in onlyfiles:
    with open(txt_path + "/" + file, encoding = 'utf-8') as f: 
        lines = f.readlines()
        new_txt = []
        sayac = 0
        for line in lines:
            lines[sayac] = line[0].replace("7","0") + line[1:]
            sayac += 1
            new_txt.append(line)
                
        newFile = open(output_path + "/" + file, "a")
        for newLine in lines:
            newFile.write(newLine) 
           
        newFile.close()  