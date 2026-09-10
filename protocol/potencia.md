# Análise de potência (pergunta 3 do portão da semana 1)

**Estado:** por preencher. Entregável da semana 1.

## O que se simula

Gerar `N` pares (efeito no relógio, efeito no tempo de vida), onde `N` é o número de intervenções
com transcriptoma **e** curva de sobrevivência, sob correlação verdadeira **0, 0.3, 0.6, 0.9**,
com o erro de medição esperado em cada eixo. Para cada cenário, medir a largura do intervalo de
confiança da **diferença emparelhada** entre o relógio de mortalidade e o relógio cronológico.

## Porquê antes de qualquer análise

O `N` do LOIO não é o número de amostras (170); é o número de **intervenções** (provavelmente
uma ou duas dezenas). Com um `N` dessa ordem, o intervalo de confiança pode ser largo ao ponto de
não distinguir correlação 0 de correlação 0.6, e nesse caso o resultado primário não consegue
responder à pergunta, independentemente do que os dados mostrem. É melhor saber isso na semana 1.

## Tabela a preencher

| Correlação verdadeira | N | Erro de medição assumido | Largura do IC 95 % da diferença | Distingue de 0? |
|---|---:|---|---|---|
| 0.0 | | | | |
| 0.3 | | | | |
| 0.6 | | | | |
| 0.9 | | | | |

## Margem escolhida

(Escrever aqui a margem que vai para o pré-registo, e a justificação. Esta é a linha que fecha
o portão.)

## Se a potência não chegar

Opções a discutir com os orientadores, por ordem de preferência:

1. Alargar a definição de intervenção (composto × dose conta como duas), aumentando o `N` à custa
   de independência entre folds, e assumir isso explicitamente.
2. Trocar o resultado primário de "diferença emparelhada" para uma pergunta de estimação
   ("qual é a correlação, com que intervalo") em vez de teste.
3. Reformular para uma pergunta que os dados sustentem.
