#!/usr/bin/env python
# -*- encoding:utf-8 -*-

print "Seja Bem vindo ao Quiz Aninmal"

# {} =  dicionario
# [] = lista
# () = Tupla = lista imutavel - nao pode ser modificada, economiza memoria

respostas = [
    {'Peixe': {
        'Ele nada?': 'Sim',
        'Ele tem pelo?': 'Nao',
        'Ele e mamifero?': 'Nao'
    },
    },
    {'Cachorro': {
        'Ele nada?': 'Nao',
        'Ele tem pelo?': 'Sim',
        'Ele e mamifero?': 'Sim'
    },
    },
]

perguntas = open("perguntas.txt")

resposta_final = {}

for pergunta in perguntas.readlines():
    pergunta = pergunta.replace('\n', '')
    resposta = raw_input(pergunta)
    resposta_final[pergunta] = resposta

# comparar dicionario de respostas com respostas certas
for animal in respostas:
    for nome_animal, perguntas_animal in animal.items():
        # http://www.tutorialspoint.com/python/dictionary_cmp.htm
        # funcao cmp - compara dicionario1 com dicionario2.
        # se dicionario1 igual dicionario2 = 0
        # se dicionario1 < dicionario2 = -1
        # se dicionario1 > dicionario2 = 1
        if cmp(resposta_final, perguntas_animal) == 0:
            print "nome animal: %s " % nome_animal
            # for c, v in perguntas_animal.items():
            #     print resposta_final
            #     print resposta_final.get(c)


