# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from math import ceil
import datetime
import time

# input do usuario
paginas = int(input("Quantas páginas/capítulos tem o livro? "))
try:
    inicio = int(input("Em qual página/capítulo você vai iniciar o livro? "))
except ValueError:
    print("*** Como não foi colocado um valor válido, preenchendo com 0")
    inicio = 0
dias = int(input("Em quantos dias quer lê-lo? "))
paginasDiarias = ceil((paginas-inicio)/dias)
comecaHoje = input("Vai começar hoje? (S/N) => ")
if comecaHoje.upper() == "S" or comecaHoje.upper() == "Y":
    primeiroDia = datetime.date.fromtimestamp(time.time())
else:
    quandoComecar = input(
        "Quando vai começar? (Escreva uma data no formato dd/mm/aaaa) => ")
    primeiroDia = datetime.datetime.strptime(quandoComecar, "%d/%m/%Y")
pularDias = input("Vai pular algum dia da semana? Quais? (Escreva os dias da semana respeitando o descrito abaixo, separando os números por vírgula sem espaço. Caso não queira pular, digite 0 ou apenas aperte \"Enter\"):\ndomingo é 7, segunda é 1, terça é 2, quarta é 3, quinta é 4, sexta é 5 e sábado é 6\n\n=> ")
pularDias = pularDias.split(",")
pularDias = [int(i) for i in pularDias]


# apos calcular o quanto de páginas o usuario deverá ler por dia o programa arrendonda pra cima e mostra o resultado
print("\nVocê vai ler {} páginas/capítulos por dia!\n".format(paginasDiarias))

# loop pra mostrar cada dia e as páginas sucessórias
diaDeLeitura = 1
diaEmQuestao = primeiroDia
while diaDeLeitura < dias+1:
    ate = (diaDeLeitura*paginasDiarias)+inicio
    
    if diaEmQuestao.isoweekday() in pularDias:
        diaEmQuestao = diaEmQuestao + datetime.timedelta(1)
        continue
    if ate > paginas:
        ate = paginas
    print(f"[ ] Dia {str(diaEmQuestao.day).zfill(2)}/{str(diaEmQuestao.month).zfill(2)}: Você vai até a página/capítulo {ate};\n")
    diaDeLeitura = diaDeLeitura + 1
    diaEmQuestao = diaEmQuestao + datetime.timedelta(1)


# A PÁGINA NO MANUAL NÃO É INCLUÍDA, VOCÊ LÊ DE FATO A PENÚLTIMA (ATÉ A 78 QUER DIZER LER A 77, MAS DEIXAR A 78 PRO OUTRO DIA)
