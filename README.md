# InfoSec-Tools
This is a a journal of sorts to document my learning of infosec and python programing. I will be adding different tools in the order that I make in hopes of looking back one day and seeing how much I've progressed. I've also attached screenshots to showcase the tools in use.
*These tools were made and tested on Kali Linux.

# Tools
1. My first tool is a password generator made in python, ([Passgen.py](https://github.com/Destituentt/InfoSec-Tools/blob/af8120a28895c8cfa1678cd7a0b37f832096fd52/Tools/Passgen.py)) that uses the **strings** and **random** libs to generate a 12 character password.
    ![image](https://github.com/Destituentt/InfoSec-Tools/assets/151950595/bde701ee-9d00-41cc-a29a-1aca54dcb62b)

2. Second tool is a simple ([UDP Client.py](https://github.com/Destituentt/InfoSec-Tools/blob/4ffdbf7c073b5dc6d8b6e49cb801ed90f32ada04/Tools/UDP%20Client.py)) to send a udp packet. To see the message, you can use netcat and use the following command ```nc -ulp 9997```
    ![image](https://github.com/Destituentt/InfoSec-Tools/assets/151950595/7b36b37e-2600-4cd3-8bc5-4a0ba47521cc)

3. Third tool is a 2 parter. This will include a ([TCPServer.py](https://github.com/Destituentt/InfoSec-Tools/blob/86c4929b7de67d269c7a839c2a1e200c9e4b3889/Tools/TCPServer.py)) and a ([TCPClient.py](https://github.com/Destituentt/InfoSec-Tools/blob/2deffc0ab4fc2c722200c65c2a4f96fe77031b92/Tools/TCPClient.py)). These two tools allow us to host a TCP Server to receive tcp packets and the client to send and acknowledge that the message was sent.
   ![image](https://github.com/Destituentt/InfoSec-Tools/assets/151950595/3f0156e4-25d4-4875-ab45-b92b924a928d)
   ![image](https://github.com/Destituentt/InfoSec-Tools/assets/151950595/c8fa060e-938b-45ef-89d6-42d244815d54)
4. Fourth tool is a simple scapy based ([PortScann.py](https://github.com/Destituentt/InfoSec-Tools/blob/d25883edcd0ac064470737cb7dcd8f8f68115da7/Tools/PortScan.py)) that will allow the user to choose a host to scan. It currently only scans for the most common ports and will report which ports are found to be open.
    ![image](https://github.com/Destituentt/InfoSec-Tools/assets/151950595/ac8a0204-8077-40f5-a4bc-b829da149a87)



