import socket
from encode_decode import encode
from RC4 import rc4_encrypt
import cv2

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf-8"
# messeage
key = b"LeDinhThuc"
image_path = "Anh_the.jpg"
hex_code = encode(image_path=image_path)
encrypt_data = rc4_encrypt(key,hex_code)
print(len(encrypt_data))
# end message
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("CLIENT_SIDE")
client.connect((HOST, SERVER_PORT))

print(f"client address: ", client.getsockname())



client.sendall(encrypt_data)

client.sendall("".encode(FORMAT))

