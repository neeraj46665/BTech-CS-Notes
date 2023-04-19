from pyperclip import copy,paste
from time import sleep
import os
path = r"/home/cid/Desktop/lafskh/code tantra/python_theory"
start_index = 1
while str(start_index) in os.listdir(path):
    start_index += 1
start_index = str(start_index)
store = path+"/"+start_index
os.mkdir(store)
text = paste()
file_index = 1
while 1:
    t = paste()
    if t == text or t=="\n" or t=="" or "galgotias" in t:
        sleep(1)
        continue
    if t == "change":
        copy("")
        start_index = str(int(start_index)+1)
        store = path + "/" + start_index
        os.mkdir(store)
        file_index=1
        continue
    text = t
    if text == "exit":
        break
    with open(store+"/"+str(file_index)+".txt","w") as f:
        f.write(text)
    file_index += 1
