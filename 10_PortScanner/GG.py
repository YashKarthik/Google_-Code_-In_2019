import socket

ip = input("Enter your ip address:   ")
for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if 0 == result:
        print("Port: {} Open".format(port))
    sock.close()