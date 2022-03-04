"""
written by : 
                    __                             __    __               _ 
   ____ ___  ____  / /_  ________  ____     ____ _/ /_  / /_  ____ ______(_)
  / __ `__ \/ __ \/ __ \/ ___/ _ \/ __ \   / __ `/ __ \/ __ \/ __ `/ ___/ / 
 / / / / / / /_/ / / / (__  )  __/ / / /  / /_/ / /_/ / /_/ / /_/ (__  ) /  
/_/ /_/ /_/\____/_/ /_/____/\___/_/ /_/   \__,_/_.___/_.___/\__,_/____/_/   
                                                                            
name of project : server-send-and-recaive-info-between-four-clinet
"""
from colorama import Fore,init
import socket
import os
import time
import sys
import threading
import random
from queue import Queue
init()

# variable
ip=''
port=0
server=None
client=None
addr=''
data=''
all_client=[]
ip_addr=[]


logo="""

███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                 
"""
print(Fore.RED+logo)
time.sleep(0.1)
print('-----------------------------------------------')
time.sleep(0.1)
while True:
    try:
        print(Fore.YELLOW+'')
        ip = input("┌─["+"ENTER IP OF SERVER"+"""]
└──╼ """+"卐 ")
        if ip==None or ip=="" or ip=="\n":
            print(Fore.RED+'the ip is empty'.upper())
            continue
        condition=str(ip).split('.')
        for dot in condition:
            if not dot.isdigit():
                print(Fore.RED+'one of the octed is not correct'.upper())
                continue

        if len(condition)!=4:
            print(Fore.RED+'your ip is not correct '.upper())
            continue

        break

    except KeyboardInterrupt:
        sys.exit()    
    except:
        print(Fore.RED+'i cant get the ip'.upper())    


# print(ip)
time.sleep(0.1)
while True:
    try:
        print(Fore.YELLOW+'')
        port = input("┌─["+"ENTER PORT OF SERVER"+"""]
└──╼ """+"卐 ")
        if port==None or port=="" or port=="\n" or port=='0':
            print(Fore.RED+'the port is empty'.upper())
            continue
        if not port.isdigit():
            print(Fore.RED+'number of port is not number'.upper())
            continue
        port=int(port)
        if port<8000 and port >9000:
            print(Fore.RED+'number of port has to be between 8000 to 9000')
            continue


        break

    except KeyboardInterrupt:
        sys.exit()    
    except:
        print(Fore.RED+'i cant get the ip'.upper())  

print('-----------------------------------------------')
time.sleep(0.1)

 
try:
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,int(port)))
    server.listen(4)
    print(Fore.GREEN+'server is running on port : '.upper(),port)
except KeyboardInterrupt:
    sys.exit()    
except:
    print(Fore.RED+'i cant bind the server'.upper())    





def handler(cli,addr):
    global data
    if addr[0] not in ip_addr:
        ip_addr.append(addr[0])
        all_client.append(cli)


    if len(ip_addr)==1:
        print(Fore.GREEN+'client with',ip_addr[0],' connect to me ')
    if len(all_client)!=2:
        print(Fore.RED+'two client have to connect to me ')
        cli.send('fail'.encode())    
        return
    if len(ip_addr)==2:
        print(Fore.GREEN+'client with ',ip_addr[1],' connected to me')    
    cli.send('connecction succussful'.encode())
    while True:
        try:  
                data=cli.recv(123456).decode()
                print(Fore.BLUE+data)
                all_client[1].send(data.encode())
        except:
                print('error')
              

while True:
    print(Fore.MAGENTA+'---------------------------------------------')
    print(Fore.CYAN+'waiting for incoming connection'.upper())
    cli,addr=server.accept()   
    threading._start_new_thread(handler,(cli,addr))




    

