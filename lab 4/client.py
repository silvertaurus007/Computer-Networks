# Import socket module 
import socket                
  

# Create a socket object 
s = socket.socket()          
# Define the port on which you want to connect 
port = 12345                

# connect to the server on local computer 
data = input("Enter String : ")
s.connect(('127.0.0.1', port)) 

s.send(data.encode())  
# receive data from the server 
print (s.recv(1024).decode()) 
# close the connection 
s.close() 
