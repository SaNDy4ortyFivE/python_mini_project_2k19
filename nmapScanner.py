import nmap, os, subprocess

class Scanner:

    available_host = []

    #defining colors
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    R = '\033[91m'
    W = '\033[0m'


    #index as choice of user as target
    index=1
    def basic_scanner(self, lan_id):

        print('Scanning for live hosts...............')


        basic_scan = nmap.PortScanner()

        basic_scan.scan(lan_id,arguments='-n -sT')

        for host in basic_scan.all_hosts():
            Scanner.available_host.append(host)

        #display the victims
        print('%sAvailable targets:%s'%(Scanner.R,Scanner.W))
        #resetting index
        Scanner.index = 1
        for host in Scanner.available_host:
            print("#{}.{}".format(Scanner.index, host))
            Scanner.index += 1


    def deep_scanner(self,index):
        deep_scan = nmap.PortScanner()
        #result is a dictionary
        result = deep_scan.scan(Scanner.available_host[index-1], arguments='-sT')
        OS_details = (result.get('scan', {}).get(str(Scanner.available_host[index-1]), {}).get('hostnames', {}))
        print('''%sTarget details:%s'''%(Scanner.R,Scanner.W))
        Open_Tcp_Ports = list(result.get('scan', {}).get(str(Scanner.available_host[index-1]), {}).get('tcp', {}).keys())
        if len(Open_Tcp_Ports) > 0:
            print('%sOpen TCP ports:%s'%(Scanner.R,Scanner.W))
            for port in Open_Tcp_Ports:
                print(port, end=', ')
        else:
            print('%sNo Open Tcp ports found:%s'%(Scanner.R,Scanner.W))
        print()
        print('*'*100)

    def deep_scan_advanced(self, index):
        print('Guessing for OS:')
        param = str(Scanner.available_host[index-1])
        res = subprocess.check_output(['sudo', 'nmap', '-O', param])
        for line in res.splitlines():
            print(line[1:])
        print('*' * 75)
        cmd = 'sudo nmap -O ' + param
        command = os.popen(cmd)
        print(command.read())
        print(command.close())

    def get_mac(self, lan_ip):
        MAC = nmap.PortScanner()
        result = MAC.scan(lan_ip)
        mac = result.get('scan', {}).get(str(lan_ip), {}).get('addresses', {}).get('mac')
        return str(mac)