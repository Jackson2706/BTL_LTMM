def initialize_state(key):
    """Khởi tạo trạng thái ban đầu của RC4 từ khóa"""
    state = list(range(256))
    j = 0

    for i in range(256):
        j = (j + state[i] + key[i % len(key)]) % 256
        state[i], state[j] = state[j], state[i]

    return state

def generate_keystream(state, length):
    """Tạo keystream từ trạng thái RC4"""
    i = 0
    j = 0
    keystream = []

    for _ in range(length):
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        keystream.append(state[(state[i] + state[j]) % 256])

    return keystream

def rc4_encrypt(key, plaintext):
    """Mã hóa văn bản bằng RC4 với khóa đã cho"""
    state = initialize_state(key)
    keystream = generate_keystream(state, len(plaintext))

    ciphertext = bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])
    return ciphertext

def rc4_decrypt(key, ciphertext):
    """Giải mã văn bản bằng RC4 với khóa đã cho"""
    return rc4_encrypt(key, ciphertext)  # Do RC4 sử dụng cùng một quá trình mã hóa và giải mã

# Sử dụng ví dụ mã hóa và giải mã
if __name__ == "__main__":
    key = b"LeDinhThuc"  # Đây là một khóa RC4 hợp lệ
    plaintext = b"Thuc chao cac ban Hello, World!"  # Văn bản cần được mã hóa

    # Mã hóa văn bản
    ciphertext = rc4_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)

    # Giải mã văn bản
    decrypted_text = rc4_decrypt(key, ciphertext)
    print("Decrypted text:", decrypted_text)
