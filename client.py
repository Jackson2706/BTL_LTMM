import socket
from DES import encrypt, generate_key, bin2hex
from encode_decode import encode, decode
import cv2

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf-8"
# messeage

image_path = "Anh_the.jpg"
hex_code = encode(image_path=image_path)
print(len(hex_code))
message = [hex_code[i:i+16] for i in range(0,len(hex_code),16)]
sender_data = ""
rkb, rk = generate_key()
for data in message: 
    print(data)
    data = str(data)[1:].upper().replace("'", "")
    encrypt_data = bin2hex(encrypt(pt = data, rkb=rkb, rk=rk))
    sender_data += encrypt_data

# end message
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("CLIENT_SIDE")
client.connect((HOST, SERVER_PORT))

print(f"client address: ", client.getsockname())



client.sendall(sender_data.encode(FORMAT))

client.sendall("".encode(FORMAT))

