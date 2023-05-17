import socket

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

    client.sendall(message.encode(FORMAT))
    # check = input("Continue? Y/N  ")
    # if check in ("Y", "y"):
    #     continue
    # else:
    #     break
