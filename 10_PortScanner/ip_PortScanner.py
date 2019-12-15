import socket

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer's Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)    

choice = input("Do you wanna scan a specific IP or your own(enter 'mine' for yours, enter 'specific' for scanning specific ip)")

if choice == 'mine':
    ip = IPAddr
elif choice == 'specific':
    ip = input("Enter IP address:  ")
    
for port in range(0, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if 0 == result:
        print("Port: {} Open 😁😁".format(port))
    else:
        print("Port: {} CLOSED ☹️☹️".format(port), "----------------------")
    sock.close()