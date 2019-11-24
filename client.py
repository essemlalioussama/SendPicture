import socket,time 
s=socket.socket()
host = "192.168.1.6"
port = 8080
s.connect((host,port))
print("connected ....")
#receive size of the picture

size = s.recv(4096).decode()
print(int(size))
time.sleep(1)
#receive the picture

picturename = input("please enter a new name for the picture : ")
picture = open(picturename,'wb')
picture_data = s.recv(int(size))
picture.write(picture_data)
picture.close()
print("picture has been received successfully")
