from struct import *
packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'
#### Don't change the code until this line ####

def int_from_bytes(b):
    return int.from_bytes(b, endieness)

def show_details():
    length = len(packet)-4*6
    sender_ID, receiver_ID, size, session_ID, message_ID, message, checksum = unpack('5i'+ str(length) + 'si', packet)
    message = message.decode('utf-8')
    print('sender_ID = ' + str(sender_ID) + ' \nmessage_ID = ' + str(message_ID) + ' \nmessage = ' + message + ' \nchecksum = ' + str(checksum) )
    pass # print sender ID (decimalm), message ID (decimal), the actual message (readable english text), and its checksum (decimal)

show_details()
