import socket,time 
s=socket.socket()
host = "192.168.1.6"
port = 8080
s.connect((host,port))
print("connected ....")
#receive size of the file

size = s.recv(4096).decode()
print(int(size))
time.sleep(1)
#receive the file

filename = input("please enter a new name for the file : ")
file = open(filename,'wb')
file_data = s.recv(int(size))
file.write(file_data)
file.close()
print("file has been received successfully")
