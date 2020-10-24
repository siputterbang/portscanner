import socket
import threading
from queue import Queue
import os
import argparse

#Nilai Default
data = ('1','2','3','4','5','6','7','8','9','0',".")
angka=0
cek = True
# Command line argument | datline =  dataline
datline =argparse.ArgumentParser()
datline.add_argument("--ip",type=str)
datline.add_argument("--p",type=int,default=10000)
datpro = datline.parse_args()
#Memasukan IP ke target scan & n utk port
target = str(datpro.ip)

for i in target:
    if i in data:
        pass
    else:
        cek = False
        break
n = datpro.p


#Antruian dengan QUEEUE || portbuk = portterbuka
antri = Queue()
portbuk = []

#Fungsi

def portscan(port):
    try:
        soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        soc.connect((target,port))
        return True
    except:
        return False

def mengantri(list_port):
    for port in list_port:
        antri.put(port)

def proses():
    while not antri.empty():
        port = antri.get()
        if portscan(port):
            print("Port {} terbuka".format(port))
            portbuk.append(port)
        else:
            pass

listt_port = range(1,n)
mengantri(listt_port)
thread_list = []

angka = target.count(".")

if angka == 3 and cek == True:
    respon = os.system('ping -c 1 ' + target)
    #10 proses/dtk
    for t in range(10):
        thread =threading.Thread(target=proses)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

if datpro.p >= 0:
    if angka ==0:
        print("--ip [IP] --p [banyak port yang akan discan,default 10000]")
    elif angka <= 3 and cek == False:
        print("IP DOWM/Tidak bisa diakses/IP anda salah")
    elif len(portbuk) == 0:print("Tidak Ada Port Yang Terbuka")




