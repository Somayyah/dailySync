#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool

os.chdir('/home/student-01-b534ea5ecda6/data/')
dest = "/home/student-01-b534ea5ecda6/data/prod_backup/"
list=[]

for path,dir,file in os.walk('prod/'):
        list.append(dir)

list=list[0]
print("List: ", list)

def backup(list):
        src = "/home/student-01-b534ea5ecda6/data/prod/"+str(list)
        print("src: {}".format(src))
        try:
                subprocess.call(["rsync", "-arq", src, dest])
        except Exception as e:
                print("exception called, {}".format(e))
if __name__=="__main__":
        p=Pool(len(list))
        p.map(backup,list)

