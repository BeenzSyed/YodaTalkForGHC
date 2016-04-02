from SOAPpy import WSDL

WSDLFILE = 'http://www.yodaspeak.co.uk/webservice/yodatalk.php?wsdl'

_server = WSDL.Proxy(WSDLFILE)

def yoda(x):
    """Yoda talk"""
    return _server.yodaTalk(x)

if __name__ == '__main__':
    import sys
    yoda(sys.argv[1])
