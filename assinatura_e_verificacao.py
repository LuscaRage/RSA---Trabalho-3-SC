import hashlib
import cifracao_e_decifracao


def assina_menssagem(message, private_key): #Assina uma mensagem com a chave privada 
    hash_value = hashlib.sha256(message).digest()
    signature = cifracao_e_decifracao.rsa_encrypt(hash_value, private_key)
    return signature

def verifica_assinatura(message, signature, public_key): #Verifica a assinatura de uma mensagem com a chave pública 
    hash_value = hashlib.sha256(message).digest()
    decrypted_signature = cifracao_e_decifracao.rsa_decrypt(signature, public_key)
    return decrypted_signature == hash_value