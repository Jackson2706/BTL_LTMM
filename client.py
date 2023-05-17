import socket
from DES import encrypt, generate_key, bin2hex

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("CLIENT_SIDE")
client.connect((HOST, SERVER_PORT))

print(f"client address: ", client.getsockname())

check_point = True
while True:
    message = input("message: ")
    rkb, rk = generate_key()
    # print(rkb)
    encrypt_data = bin2hex(encrypt(pt = message, rkb=rkb, rk=rk))
    print(f"encrypt data: {encrypt_data}")
    client.sendall(encrypt_data.encode(FORMAT))
    # check = input("Continue? Y/N  ")
    # if check in ("Y", "y"):
    #     continue
    # else:
    #     break