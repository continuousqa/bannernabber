__author__ = 'bwarner'
import socket
import sys

socket.setdefaulttimeout(0.01)
# Base class is the scan class. This will be used to initiate the object and set up the expected variables
class Scan(object):
    def __init__(self, host, start_port,end_port):
        self.host = host
        self.start_port = start_port
        self.end_port = end_port

# Machine is a class inhereting from Scan.  When we call it and pass in host,start port, end port - it
# initializes by it's inheritence with Scan.
class Machine(Scan):
    def check_port(self):
        # for loop iterates over a range (defined as the supplied start and end ports)
        for port in range(self.start_port, self.end_port):

            # this is the call to attempt to check the socket on a port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect = sock.connect_ex((self.host, port))
            if connect == 0:
                print("Port " + repr(port) + " : Open")
                try:
                    sock.send(bytes("GET\n", 'UTF-8')) # For fun we can send some data!
                    print(bytes('         ', 'UTF-8') + sock.recv(1024))
                except socket.gaierror:
                    print("Hostname could not be resolved")

                except socket.error:
                    print("          <No Banner Returned>")
                sock.close()


params = len(sys.argv)
if params < 4:
    print('You could: python3 scan.py <ip address> <starting port> <ending port> to scan. \n')
    uip = input('Enter IP address to scan: ')
    upt = input('Enter starting port #: ')
    upt2 = input('Enter ending port #: ')
    new_scan = Machine(uip,int(upt),int(upt2))
else:
    uip = (str(sys.argv[1]))
    upt = int(sys.argv[2])
    upt2 = int(sys.argv[3])
    new_scan = Machine(uip, upt, upt2)

new_scan.check_port()

