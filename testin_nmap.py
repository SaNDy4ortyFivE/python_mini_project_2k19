import nmap
scan = nmap.PortScanner()
result = scan.scan('192.168.43.1', arguments='-sU')
print(result)
print(result.get('scan', {}).get('192.168.43.1', {}).get('addresses', {}).get('mac'))
x = list(result.get('scan', {}).get('192.168.43.1', {}).get('udp', {}).keys())
if(len(x)>0):
    print(x[0])
else:
    print('all ports closed')
