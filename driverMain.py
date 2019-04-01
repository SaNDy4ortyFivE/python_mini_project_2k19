#importing all written scripts
import nmap,scapy
import nmapScanner, scapy_main_file, banner, os




def main():

    os.system('clear')

    #defining colors
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    R = '\033[91m'
    W = '\033[0m'

    banner.banner_print()
    #fun starts here
    #do the basic scan on the network all the 256 ip addresses

    #creatin object for nmapScanner class
    scanner = nmapScanner.Scanner()
    lan_id = input('Enter lan:%s'%(W))

    #take the lan_id for getting wifi mac address,it will be needed for scapy later
    print('%sGetting MAC address for entered lan.............'%(B))
    mac = scanner.get_mac(lan_id)
    print('Captured lan MAC')

    temp = lan_id

    if not lan_id.endswith('/24'):
        lan_id = lan_id + '/24 --exclude ' + str(temp)
    scanner.basic_scanner(lan_id)
    print('*'*100)
    #choose target
    target_index = int(input('%sEnter traget(index)%s:'%(R,W)))

    #ask if deep scan is to be performed or skip it
    deep_scan_choice = input('%sperform (Y)deep scan or enter to skip to attack section:%s'%(R,W)).lower()
    print('*'*100)
    if deep_scan_choice=='y':
        scanner.deep_scanner(target_index)
        scanner.deep_scan_advanced(target_index)
    print('*'*100)

    #getting target mac
    target_mac = scanner.get_mac(str(scanner.available_host[target_index-1]))
    print('''%s
        welcome to attack section:
        1)Deauthentication attack
        2)MITM
        3)Phishing
    
        choose a attack:%s'''%(R,W))
    choice = int(input())

    get_scapy = scapy_main_file.scapy_scapy()

    if choice == 1:
        get_scapy.deauth(mac, target_mac)






if __name__=='__main__':
    main()