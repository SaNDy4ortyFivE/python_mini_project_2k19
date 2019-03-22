import nmap, os, subprocess

class Scanner:

    available_host = []

    #index as choice of user as target
    index=1
    def basic_scanner(self, lan_id):
        basic_scan = nmap.PortScanner()

        basic_scan.scan(lan_id)

        for host in basic_scan.all_hosts():
            Scanner.available_host.append(host)

        #display the victims
        print('Available targets:')
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
        print('Target details:', OS_details)
        Open_Tcp_Ports = list(result.get('scan', {}).get(str(Scanner.available_host[index-1]), {}).get('tcp', {}).keys())
        if len(Open_Tcp_Ports) > 0:
            print('Open TCP ports:', end='')
            for port in Open_Tcp_Ports:
                print(port, end=', ')
        else:
            print('No Open Tcp ports found:')
        print()
        print('*'*75)

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