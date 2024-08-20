#Crie um dicionário para armazenar informaçoes de um livro

from typing import Dict, Any

livro1: Dict[str, any] = {
    "Titulo": "Game of thrones",
    "Autor": "Estagiário",
    "Ano": 2005
}

livro2: Dict[str, any] = {
    "Titulo": "analise de dados",
    "Autor": "Estagiário2",
    "Ano": 2011
}

livro3: Dict[str, any] = {
    "Titulo": "agate christie",
    "Autor": "Estagiário3",
    "Ano": 2007
}


lista_de_livros = []

lista_de_livros.append(livro1)
lista_de_livros.append(livro2)
lista_de_livros.append(livro3)




print(lista_de_livros)



