
# 🔐 File Encryptor/Decryptor with AES and Python

Este projeto contém dois scripts em Python que realizam a **criptografia** e **descriptografia** de arquivos utilizando o algoritmo AES (CTR mode), com o uso de variáveis de ambiente para configuração.

## 🛡️ Segurança

Este projeto é **apenas educacional**. Evite utilizar esse método para proteger dados sensíveis em produção. Para aplicações reais, considere bibliotecas mais robustas como `cryptography` e políticas adequadas de gerenciamento de chaves.

## 📁 Estrutura

- `encrypter.py` – Criptografa um arquivo e o salva com uma nova extensão.
- `decrypter.py` – Descriptografa o arquivo criptografado e o restaura com o nome original.

---

## ⚙️ Variáveis de Ambiente

Antes de executar os scripts, é necessário configurar um arquivo `.env` com as variáveis descritas no arquivo `.env.example`

---

## 🛠️ Como Usar

### 🔒 Criptografar um arquivo

1. Execute o script de criptografia:

```bash
python {path}/encrypter.py
```

2. O arquivo original será **removido** e o arquivo criptografado será salvo com a extensão definida.

---

### 🔓 Descriptografar um arquivo

1. Execute o script de descriptografia:

```bash
python {path}/decrypter.py
```

2. O arquivo criptografado será **removido** e o arquivo original será restaurado.

---

## 🧪 Requisitos

- Python 3+
- [pyaes](https://pypi.org/project/pyaes/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Instalação dos pacotes:
```bash
pip install pyaes python-dotenv
```

---
