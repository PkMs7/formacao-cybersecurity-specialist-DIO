import os
from dotenv import load_dotenv
import pyaes

## Carrega variáveis de ambiente do arquivo .env
load_dotenv()

## Abrir o arquivo a ser criptografado
file_path = os.environ['FILE_PATH']
file = open(file_path, 'rb')
file_data = file.read()
file.close()

## Remover o arquivo a ser criptografado
os.remove(file_path)

## Importar a chave de criptografia
key = os.environ['CRYPTO_KEY']
aes = pyaes.AESModeOfOperationCTR(key.encode('utf-8'))

## Criptografar arquivo a ser criptografado
crypto_data = aes.encrypt(file_data)

## Salvar o arquivo criptografado
new_file = file_path + os.environ['FILE_EXTENSION']
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()