from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(text):
    """Thêm byte để đảm bảo độ dài của văn bản là bội số của 16"""
    return text + b"\0" * (AES.block_size - len(text) % AES.block_size)

def encrypt(key, plaintext):
    """Mã hóa văn bản bằng AES với khóa đã cho"""
    plaintext = pad(plaintext)
    iv = get_random_bytes(AES.block_size)  # Tạo một vectơ khởi đầu ngẫu nhiên
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)
    return iv + ciphertext

def decrypt(key, ciphertext):
    """Giải mã văn bản bằng AES với khóa đã cho"""
    iv = ciphertext[:AES.block_size]  # Lấy vectơ khởi đầu từ đầu mã hóa
    ciphertext = ciphertext[AES.block_size:]  # Lấy phần còn lại của mã hóa
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.rstrip(b"\0")

# Sử dụng ví dụ mã hóa và giải mã
if __name__ == "__main__":
    key = b"ledinhthuc123456"  # Đây là một khóa AES hợp lệ có độ dài 16 byte (128 bit)
    plaintext = b"Hello, World!"  # Văn bản cần được mã hóa
    print(type(plaintext))

    # Mã hóa văn bản
    ciphertext = encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)

    # Giải mã văn bản
    decrypted_text = decrypt(key, ciphertext)
    print("Decrypted text:", decrypted_text)
