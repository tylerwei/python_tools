#-*- encoding:UTF-8 -*-
import socket,time,sys,getopt
from optparse import OptionParser


def main():
    apikey = None
    url = None
    usage = "usage: python %prog -a apikey -u url\n       python %prog --apikey apikey --url url"
    parser = OptionParser(usage)
    parser.add_option("-a", "--apikey", action="store", type="string", dest="apikey",
            help="input your apikey")
    parser.add_option("-u", "--url", action="store", type="string", dest="url",
            help="input the report url")
    (options, args) = parser.parse_args()
    if len(sys.argv) != 5:
        parser.error("incorrect number of arguments")
    apikey = options.apikey
    url = options.url
    try:
        HOST = socket.gethostbyname(url)
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
        print "Please check your network, can't connect to localhost"
    sock.close()

if __name__ == '__main__':
    main()
