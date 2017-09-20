
# pydashdoorbell

pydashdoorbell is a program which sends a text message to your phone when an Amazon Dash button is pressed.  It works great as a doorbell if you have dogs or young kids.  
<br>

# Requirements

- **Amazon Dash button +**
- **Python 2.7 +**
- **Scapy +**
- **Twilio +**
<br>

# How to Use
Create an account with [Twilio](https://www.twilio.com/) to receive a SID, AuthToken and twilio phone number.  Connect the Dash button to your wifi using the Amazon app on your phone - make sure not to select a product otherwise you may inadvertently end up purchasing somehting every time you press the button...
Once connected to wifi, locate the Dash MAC address in your router's log or DHCP table.

Now, fill in *account_sid*, *auth_token*, *to_phone_num* (phone you want to receive texts with), *from_phone_num* (Twilio number), and *dash_mac_address* located at the top of **dash_sms_doorbell.py** and run it as root (sudo in Linux).
