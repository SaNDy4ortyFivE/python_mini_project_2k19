#importing all written scripts
import nmap
import nmapScanner

tool_name = 'nOTORIOUS_nETWORKER'
#current developers
authors = ['sandy_45','s_$']
#tool description
description='''a tool to own a network and be a NOTORIOUS one '''

list_of_attacks = ['Deep Scan']

def main():
    #printing the decription of the tool
    #print('\033[1;32;40m')
    print(tool_name.center(75, '#'))

    '''print('authors->',end='')
    for auth in authors:
        print(auth,end=' ')
    print()
    print('#'*40)'''

    #fun starts here
    #do the basic scan on the network all the 256 ip addresses

    #creatin object for nmapScanner class
    scanner = nmapScanner.Scanner()
    lan_id = input('Enter lan:')
    if not lan_id.endswith('/24'):
        lan_id = lan_id + '/24'
    scanner.basic_scanner(lan_id)
    print('*'*75)
    #choose target
    target_index = int(input('Enter traget(index):'))

    #ask if deep scan is to be performed or skip it
    deep_scan_choice = input('perform (Y)deep scan or enter to skip to attack section:').lower()
    print('*'*75)
    if deep_scan_choice=='y':
        scanner.deep_scanner(target_index)
        scanner.deep_scan_advanced(target_index)
    print('*'*75)
    print('welcome to attack section:')






if __name__=='__main__':
    main()