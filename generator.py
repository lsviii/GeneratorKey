import os
from base64 import b64encode

gerar8 = os.urandom(8)
gerar16 = os.urandom(16)

gerado8 = b64encode(gerar8).decode('utf-8')
gerado16 = b64encode(gerar16).decode('utf-8')


print("Código com 8 caracteres: " + gerado8)

print("Código com 16 caracteres" + gerado16)