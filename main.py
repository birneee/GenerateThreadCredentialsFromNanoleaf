# inspired by https://www.reddit.com/r/homeassistant/comments/11pkmpu/comment/jzjtxbo/
from python_otbr_api import tlv_parser
from python_otbr_api.tlv_parser import MeshcopTLVItem

print('1. Go to Nanoleaf App on iOS > More > Thread Networks > Your Network')
print('2. Enter the following:')

# Apple
CHANNEL = int(input('Channel: '))
PANID = input('PAN ID: ')
EXTPANID = input('Extended PAN ID: ')
NETWORK_KEY = input('Network Key: ')
TIMESTAMP = b'\x00\x00\x00\x00\x00\x03\x00\x00'

channel = MeshcopTLVItem(tag=0, data=CHANNEL.to_bytes(length=3, byteorder='big'))
pan_id= MeshcopTLVItem(tag=1, data=bytes.fromhex(PANID))
ext_pan_id = MeshcopTLVItem(tag=2, data=bytes.fromhex(EXTPANID))
network_key = MeshcopTLVItem(tag=5, data=bytes.fromhex(NETWORK_KEY))
timestamp = MeshcopTLVItem(tag=14, data=TIMESTAMP)

tlv_new = {0: channel, 1: pan_id, 2:ext_pan_id, 4: network_key, 14: timestamp}
tlv = tlv_parser.encode_tlv(tlv_new)

print('3. Go to Home Assistant > Integrations > Thread > Configure > More > Add dataset from TLV')
print('4. Enter the following TLV:')
print(tlv)
