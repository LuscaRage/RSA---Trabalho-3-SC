import math


def rsa_encrypt(message, public_key): # Cria um critograma a partir da mensagem e da chave pública RSA
    n, e = public_key
    padded_message = pad_message(message, n.bit_length() // 8)
    m = int.from_bytes(padded_message, "big")
    c = pow(m, e, n)
    return c.to_bytes((c.bit_length() + 7) // 8, "big")

def pad_message(message, key_length):  #Adiciona o padding OEAP na mensagem.
    if len(message) > key_length - 2 * math.ceil(math.log2(key_length) / 8) - 2:
        raise ValueError("Tamanho da mensagem excede o limite suportado.")
    
    pad_length = key_length - len(message) - 2 * math.ceil(math.log2(key_length) / 8) - 2
    padding = b"\x00" * pad_length

    return b"\x00" + padding + b"\x01" + padding + message


def rsa_decrypt(ciphertext, private_key): #Retorna a mensagem original a partir do criptograma e da chave privada RSA
    n, d = private_key
    c = int.from_bytes(ciphertext, "big")
    m = pow(c, d, n)
    padded_message = m.to_bytes((m.bit_length() + 7) // 8, "big")
    return unpad_message(padded_message)

def unpad_message(padded_message): #Retira o padding OEAP da mensagem.
    padding_start = padded_message.rindex(b"\x00") + 1
    return padded_message[padding_start:]

