from scapy.all import *
from twilio.rest import Client
import time

account_sid = ""
auth_token = ""
to_phone_num = ""
from_phone_num = ""
dash_mac_address = ""

client = Client(account_sid, auth_token)



def arp_detect(pkt):
    if (pkt.haslayer(ARP)):
        if pkt[ARP].hwsrc == dash_mac_address:
            #print pkt[ARP].hwsrc
            print 'Dash Button Detected'
            message = client.api.account.messages.create(to=to_phone_num,
                                                         from_=from_phone_num,
                                                         body="Dash Button Detected")
            time.sleep(5*60)  # 5 minutes


print(sniff(prn=arp_detect, filter="arp", store=0))
