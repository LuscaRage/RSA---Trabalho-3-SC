import base64
import chave
import cifracao_e_decifracao
import assinatura_e_verificacao

#Menu de escolhas
opcao = int(input("\n Escolha uma das opções:\n1) Gerar chaves (mínimo de 1024 bits) \n2) Cifração assimétrica RSA usando OAEP\n3) Decifração assimétrica RSA usando OAEP \n4) Assinatura da mensagem (cifração do hash) \n5) Verificação (comparação do hash)\n"))

if opcao == 1:
    chave_publica, chave_privada = chave.gerar_senhas()
    print("\nChave Pública:", chave_publica)
    print("\nChave Privada:", chave_privada)

if opcao == 2:
    menssagem = input("\nDigite:\nMensagem a ser criptografada: ").encode()
    chave_publica = input("Chave Pública: ").strip().split(',')
    chave_publica = (int(chave_publica[0]), int(chave_publica[1]))
    ciphertext = base64.b64encode(cifracao_e_decifracao.rsa_encrypt(menssagem, chave_publica))
    
    print("\nMensagem criptografada:", ciphertext.decode())

if opcao == 3:
    encrypted_message_base64 = input("\nDigite:\nMensagem criptografada: ").encode()
    private_key = input("Chave Privada: ").strip().split(',')
    private_key = (int(private_key[0]), int(private_key[1]))
    decrypted_message = cifracao_e_decifracao.rsa_decrypt(base64.b64decode(encrypted_message_base64), private_key)
    print("\nMensagem descriptografada:", decrypted_message.decode())

if opcao == 4:
    message = input("Digite:\nMensagem a ser assinada: ").encode()
    private_key = input("Chave Privada: ").strip().split(',')
    private_key = (int(private_key[0]), int(private_key[1]))
    signature = base64.b64encode(assinatura_e_verificacao.assina_menssagem(message, private_key))
    print("Assinatura:", signature.decode())

if opcao == 5:
    message = input("\nDigite:\nMensagem original: ").encode()
    signature_base64 = input("\nAssinatura: ").encode()
    public_key = input("Chave Pública: ").strip().split(',')
    public_key = (int(public_key[0]), int(public_key[1]))
    signature = base64.b64decode(signature_base64)
    is_valid = assinatura_e_verificacao.verifica_assinatura(message, signature, public_key)
    print("\nA assinatura é")
    if is_valid:
        print(" válida.")
    else:
        print(" inválida.")