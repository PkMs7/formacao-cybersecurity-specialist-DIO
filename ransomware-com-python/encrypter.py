import os
from dotenv import load_dotenv
import pyaes

## Carrega variáveis de ambiente do arquivo .env
load_dotenv()

## Abrir o arquivo criptografado
file_name = os.environ['FILE_NAME']
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remover o arquivo
os.remove(file_name)

## Chave de criptografia
key = os.environ['CRYPTO_KEY']
aes = pyaes.AESModeOfOperationCTR(key.encode('utf-8'))

## Criptografar arquivo
crypto_data = aes.encrypt(file_data)

## Salvar o arquivo criptografado
new_file = file_name + os.environ['FILE_EXTENSION']
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()