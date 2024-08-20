from typing import Dict, Any
import json


lista: list = ["Sapato", 39, 299.90, True]

produto01: dict = {
    "nome":"Sapato",
    "quantidade":39,
    "preco":299.90,
    "disponibilidade": True
}

produto02: dict = {
    "nome":"camiseta",
    "quantidade":10,
    "preco":149.90,
    "disponibilidade": False
}


carrinho: list = []

carrinho.append(produto01)
carrinho.append(produto02)



carrinho_json = json.dumps(carrinho)
print(carrinho_json)


