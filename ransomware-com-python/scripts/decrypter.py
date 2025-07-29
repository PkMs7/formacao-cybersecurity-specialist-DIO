import os
from dotenv import load_dotenv
import pyaes

## Carrega variáveis de ambiente do arquivo .env
load_dotenv()

## Abrir o arquivo criptografado
file_path = os.environ['FILE_PATH_CRYPTO']
file = open(file_path, 'rb')
file_data = file.read()
file.close()

## Remover o arquivo criptografado
os.remove(file_path)

## Importar a chave para descriptografia
key = os.environ['CRYPTO_KEY']
aes = pyaes.AESModeOfOperationCTR(key.encode('utf-8'))

## Descriptografar o arquivo criptografado
decrypt_data = aes.decrypt(file_data)

## Salvar o arquivo descriptografado
new_file = os.environ['FILE_PATH']
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()

