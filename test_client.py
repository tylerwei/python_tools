#-*- encoding:UTF-8 -*-
import socket,time,sys,getopt
from optparse import OptionParser


def main():
    apikey = None
    domain = None
    usage = "usage: python %prog -a apikey -d domain\n       python %prog --apikey apikey --domain \
domain\n\nexample: python %prog -a my_apikey -d baidu.com"

    parser = OptionParser(usage)
    parser.add_option("-a", "--apikey", action="store", type="string", dest="apikey",
            help="input your apikey")
    parser.add_option("-d", "--domain", action="store", type="string", dest="domain",
            help="input the report host")
    (options, args) = parser.parse_args()
    if len(sys.argv) != 5:
        parser.error("incorrect arguments")
    apikey = options.apikey
    domain = options.domain
    try:
        HOST = socket.gethostbyname(domain)
    except:
        print "Please check your settings of dns\n"
        exit(1)

    PORT = 2003
    BUFFER = 1024
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print "Create socket error"
        exit(1)

    sock.settimeout(5)
    try:
        sock.connect((HOST, PORT))
        sock.send("%s/test.dnspod.com/127.0.0.1/test 1 %d" % (apikey, int(time.time())))
        recv = sock.recv(BUFFER)
        print "Network is Ok, recv is :%s" % recv
    except:
        print "Please check your argments or network or dns settings,\n \
The ip of [%s] is:%s, \
can't connect to localhost" % (domain, HOST)
    sock.close()

if __name__ == '__main__':
    main()
