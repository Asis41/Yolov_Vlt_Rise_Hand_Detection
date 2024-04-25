import cv2
import socket
import pickle 
import os
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,1000000)

server_ip = "127.0.0.1"
server_port = 6666

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

while cap.isOpened():

    ret , img = cap.read()

    cv2.imshow('Img Client',img)

    ret, buffer = cv2.imencode(".jpg", img, [int(cv2.IMWRITTE_JPEG_QUALITY),30])

    x_as_bytes = pickle.dumps(buffer)

    s.sendto((x_as_bytes),(server_ip,server_port))

    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()


import cv2
import socket
import pickle 
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
port = 6666  
s.bind((ip,port))

while True:
    x = s.recvfrom(1000000)
    clientip = x[1][0]
    data = x[0]

    data = pickle.loads(data)

    img = cv2.imdecode(data, cv2.IMREAD_COLOR)

    cv2.imshow('Img Server', img)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()