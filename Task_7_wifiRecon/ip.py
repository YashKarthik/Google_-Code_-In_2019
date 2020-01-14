import nmap

class Network(object):
    def __init__(self):
        ip = input("enter ip: ")
        self.ip = ip

    def networkscanner(self):
        network = self.ip + '/24'

        print("Scanning------->")

        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        host_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in host_list:
            print("Host\t{}".format(host))

if __name__ == '__main__':
    D = Network()
    D.networkscanner()
        
