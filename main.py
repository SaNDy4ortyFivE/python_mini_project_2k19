#importing all written scripts
import nmap,scapy
import nmapScanner, scapy_main_file, banner, os


def main():
    os.system('clear')
    banner.banner_print()


    #defining colors
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    R = '\033[91m'
    W = '\033[0m'

    choice = int(input())

    if choice == 1:
        word_input = input('Enter Hash:')
        os.system('./a.out words %s'%(word_input))


    elif choice ==2:
        # creatin object for nmapScanner class
        scanner = nmapScanner.Scanner()
        lan_id = input('Enter lan:%s' % (W))

        # take the lan_id for getting wifi mac address,it will be needed for scapy later
        print('%sGetting MAC address for entered lan.............' % (B))
        mac = scanner.get_mac(lan_id)
        print('LAN MAC captured:',mac)

        temp = lan_id

        if not lan_id.endswith('/24'):
            lan_id = lan_id + '/24 --exclude ' + str(temp)

        scanner.basic_scanner(lan_id)
        print('*' * 100)
        # choose target
        target_index = int(input('%sEnter target(index)%s:' % (R, W)))

        # ask if deep scan is to be performed or skip it
        deep_scan_choice = input('%sperform (Y)deep scan or enter to skip to attack section:%s' % (R, W)).lower()
        print('*' * 100)
        if deep_scan_choice == 'y':
            scanner.deep_scanner(target_index)
            scanner.deep_scan_advanced(target_index)
        print('*' * 100)


    elif choice == 3:

        iface = input('Enter interface name:')

        get_scapy = scapy_main_file.scapy_scapy()

        scanner = nmapScanner.Scanner()
        lan_id = input('Enter lan:%s' % (W))

        # take the lan_id for getting wifi mac address,it will be needed for scapy later
        print('%sGetting MAC address for entered lan.............' % (B))
        mac = scanner.get_mac(lan_id)
        print('LAN MAC captured:', mac)

        temp = lan_id

        if not lan_id.endswith('/24'):
            lan_id = lan_id + '/24 --exclude ' + str(temp)

        scanner.basic_scanner(lan_id)
        print('*' * 100)
        # choose target
        target_index = int(input('%sEnter target(index)%s:' % (R, W)))

        target_mac = scanner.get_mac(scanner.available_host[target_index-1])

        get_scapy.deauth(mac, target_mac, iface)


















if __name__=="__main__":
    main()
