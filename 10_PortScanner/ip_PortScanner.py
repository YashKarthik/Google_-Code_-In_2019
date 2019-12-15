import socket
import requests

class PortScanner:
    def __init__(self, hostname, IPAddr, ip, choice, result, port, sock, IP):
        self.hostname = hostname
        self.IPAddr = IPAddr
        self.ip = ip
        self.choice = choice
        self.result = result
        self.port = port
        self.sock = sock
        self.IP = IP
        

    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    ip = requests.get('https://checkip.amazonaws.com').text.strip()
    print("Your Computer's Name is: " + hostname)    
    print("Your Computer IP Address is: ", IPAddr)    
    print("Your external IP address is: ", ip)

    choice = input("Which do you wanna scan? (enter '1' for your computer's, enter '2' for your external IP addresss, enter '3' for scanning specific ip)  ")

    if choice == 1:
        IP = IPAddr
    elif choice == 2:
        IP = ip
    elif choice == 3:
        IP = input("Enter IP address:  ")
    
    for port in range(0, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((IP, port))
        if 0 == result:
            print("Port: {} Open 😁 😁".format(port))
        else:
            print("Port: {} CLOSED ☹️☹️".format(port), "----------------------")
        sock.close()