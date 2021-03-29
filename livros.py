# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from math import ceil
import datetime
import time

#input do usuario
paginas = int(input("Quantas páginas/capítulos tem o livro? "))
try:
    inicio = int(input("Em qual página/capítulo você vai iniciar o livro? "))
except ValueError:
    inicio = 0
dias = int(input("Em quantos dias quer lê-lo? "))
paginasDiarias = ceil((paginas-inicio)/dias)
hoje = datetime.date.fromtimestamp(time.time())

#apos calcular o quanto de páginas o usuario deverá ler por dia o programa arrendonda pra cima e mostra o resultado
print("\nVocê vai ler {} páginas/capítulos por dia!\n".format(paginasDiarias))

#loop pra mostrar cada dia e as páginas sucessórias
for dia in range(1, dias+1):
    ate = (dia*paginasDiarias)+inicio
    td = datetime.timedelta(dia-1)
    diaEmQuestao = hoje + td
    if ate > paginas:
        ate = paginas
    print(f"Dia {str(diaEmQuestao.day).zfill(2)}/{str(diaEmQuestao.month).zfill(2)}: Você vai até a página/capítulo {ate};")

# A PÁGINA NO MANUAL NÃO É INCLUÍDA, VOCÊ LÊ DE FATO A PENÚLTIMA (ATÉ A 78 QUER DIZER LER A 77, MAS DEIXAR A 78 PRO OUTRO DIA)