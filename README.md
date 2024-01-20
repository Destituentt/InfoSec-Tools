# InfoSec-Tools
This is a a journal of sorts to document my learning of infosec and python programing. I will be adding different tools in the order that I make in hopes of looking back one day and seeing how much I've progressed.

# Tools
1. My first tool is a password generator made in python, ([Passgen.py](https://github.com/Destituentt/InfoSec-Tools/blob/af8120a28895c8cfa1678cd7a0b37f832096fd52/Tools/Passgen.py)) that uses the **strings** and **random** libs to generate a 12 character password.
    ![image](https://github.com/Destituentt/InfoSec-Tools/assets/151950595/bde701ee-9d00-41cc-a29a-1aca54dcb62b)

2. Second tool is a simple ([UDP Client.py](https://github.com/Destituentt/InfoSec-Tools/blob/4ffdbf7c073b5dc6d8b6e49cb801ed90f32ada04/Tools/UDP%20Client.py)) to send a udp packet. To see the message, you can use netcat and use the following command ```nc -ulp 9997```
3. Third tool will be a 2 parter. This will include a ([TCPServer.py](https://github.com/Destituentt/InfoSec-Tools/blob/86c4929b7de67d269c7a839c2a1e200c9e4b3889/Tools/TCPServer.py)) and a ([TCPClient.py](https://github.com/Destituentt/InfoSec-Tools/blob/2deffc0ab4fc2c722200c65c2a4f96fe77031b92/Tools/TCPClient.py)). These two tools allow us to host a TCP Server to receive tcp packets and the client to send and acknowledge that the message was sent. 
