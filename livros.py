# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from math import ceil

#input do usuario
paginas = int(input("Quantas páginas/capítulos tem o livro? "))
dias = int(input("Em quantos dias quer lê-lo? "))
paginasDiarias = ceil(paginas/dias)

#apos calcular o quanto de páginas o usuario deverá ler por dia o programa arrendonda pra cima e mostra o resultado
print("\nVocê vai ler {} páginas/capítulos por dia!\n".format(paginasDiarias))

#loop pra mostrar cada dia e as páginas sucessórias
for dia in range(1, dias+1):
    if paginasDiarias*dia >= paginas:
        print("Dia {}: Você termina o livro lendo até a página/capítulo {}".format(dia, paginas))
        break
    else:
        print("Dia {}: ler até página/capítulo {}".format(dia, paginasDiarias*dia))
