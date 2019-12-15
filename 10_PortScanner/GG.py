import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer's Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)    