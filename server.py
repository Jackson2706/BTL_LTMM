import socket
from DES import bin2hex, generate_key, encrypt
HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, SERVER_PORT))
s.listen()

print("SERVER SIDE")
print(f"server: {HOST} {SERVER_PORT}")
conn, addr = s.accept()

check_point = False
while True:
    if check_point:
        conn, addr = s.accept()

    print(f"client address: {addr}")
    print("conn: ", conn.getsockname())
    rkb, rk = generate_key()
    print(rkb)
    message = conn.recv(1024).decode(FORMAT)
    if len(message):
        rkb_rev = rkb[::-1]
        rk_rev = rk[::-1]
        text = bin2hex(encrypt(message, rkb_rev, rk_rev))
        print(f"message: {text}")
        check_point = False
    else:
        check_point = True
        conn.close()
    print("---"*20)