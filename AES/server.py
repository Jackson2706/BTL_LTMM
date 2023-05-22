import socket
from encode_decode import decode
from AES import decrypt
import cv2

key = b"ledinhthuc123456"
HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, SERVER_PORT))
s.listen()

print("SERVER SIDE")
print(f"server: {HOST} {SERVER_PORT}")
conn, addr = s.accept()
receive_data = ""
check_point = False
while True:
    if check_point:
        conn, addr = s.accept()

    print(f"client address: {addr}")
    print("conn: ", conn.getsockname())
    # print(rkb)
    message = conn.recv(100000)
    if len(message):
        # message = codecs.decode(message, 'hex').decode('utf-8')
        data = decrypt(key, message)
        print(f"message: {data}")
        print(type(data))
        print(len(data))
        # check_point = False
    else:
        check_point = True
        conn.close()
        break
    print("---"*20)
# print(receive_data)
# print(len(receive_data))
# split_data = [receive_data[i:i+16] for i in range(0, len(receive_data), 16)]
# decode_data = b''
# for data in split_data:
#     print(data)
    
#     rkb_rev = rkb[::-1]
#     rk_rev = rk[::-1]
#     text = bin2hex(encrypt(data, rkb_rev, rk_rev))
#     hex_code = bytes(text, encoding='utf-8')
#     decode_data += hex_code


image = decode(data)
print(image)
# Hiển thị ảnh
cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()