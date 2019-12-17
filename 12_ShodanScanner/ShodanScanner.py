import shodan
import sys
import socket

api = shodan.Shodan('B37FoQIeHcfOarldXp7H7a2vzqZg5BrF')

#Search the target by their IP address
def HostIP():
    host_inp = input("Enter target's IP addrtess: ")
    host = api.host(host_inp)

    print("""
IP: {}
Organisation: {}
Operating System: : {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

    for item in host ['data']: 
        print(""" 
Port: {}
Banner: {}
-
              """.format(item['port'], item['data']))

#Search the target by their hostname
def ShodanScan():   
    try:
        target = input("Enter the target's hostname: ")
        results = api.search(target)

        print("Results found: {}".format(results['total']))
        for results in results['matches']:
            print('IP: {}'.format(results['ip_str']))
            print(results['data'])
            print('----------------------')
    except shodan.APIError as e:
        print('Error: {}'.format(e))

def MyIP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("your IP address: ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 

choice = 1

while choice != 0:
    choice = int(input("""_________________________________
Enter 1 - To get your IP.
Enter 2 - To scan a specific IP address.
Enter 3 - To Shodan scan using hostname.
Enter 0 - To exit the script.

INPUT: """))

    if choice == 1:
        MyIP()
    elif choice == 2:
        HostIP()
    elif choice == 3:
        ShodanScan()
        
if choice == 0:
    print("-----------------EXITTING PROGRAM---------------")


