import socket

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, SERVER_PORT))
s.listen()

print("SERVER SIDE")
print(f"server: {HOST} {SERVER_PORT}")


while True:
    conn, addr = s.accept()

    print(f"client address: {addr}")
    print("conn: ", conn.getsockname())
    message = conn.recv(1024).decode(FORMAT)
    print(len(message))
    if len(message):
        print(f"message: {message}")
    else:
        conn.close()