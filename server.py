import socket,os,Takephoto,time
s = socket.socket()
host = "192.168.1.6"
port = 8080
s.bind((host,port))
s.listen(1)
print("waiting for any incoming connections ...")
conn , addr = s.accept()
print(addr,"Has connected to the server")
picturename = Takephoto.takeShot()
#send size of the file
statinfo = os.stat(picturename)
size = statinfo.st_size
conn.send(str(size).encode())
print(size)
time.sleep(1)
#send the file
picture = open(picturename,"rb")
picture_data = picture.read(size)
conn.send(picture_data)
print("data has transmitted successfully")
