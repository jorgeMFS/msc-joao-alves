# Guião da reunião com o João Alves (10 de setembro de 2026)

Objetivo da reunião. O João sair a saber (1) qual é a pergunta da tese, (2) porque é que a pergunta existe, (3) o que faz esta semana, (4) onde fica o trabalho.

Tempo previsto, 45 a 60 minutos. Cada bloco tem o que dizes e uma pergunta para confirmar que ele percebeu.

---

## 1. O problema de fundo (5 min)

**O que dizer.**
Se queremos saber se um fármaco faz um ratinho viver mais, temos de esperar que o ratinho morra. Isso são três anos por fármaco, e é por isso que quase nada é testado. A ideia do campo é encontrar algo que se meça num animal ainda vivo e que dê a resposta mais cedo. Esse algo é a atividade dos genes no fígado.

**Pergunta ao João.** Porque é que não se testa simplesmente tudo em ratinhos até morrerem? (resposta esperada, tempo e custo)

---

## 2. O que é um relógio de envelhecimento (10 min)

**O que dizer.**
Tira se um pedaço de fígado a um ratinho e mede se quantas cópias de mRNA existem de cada gene. Um gene que a célula está a usar muito produz milhares de cópias, um gene parado produz quase nenhuma. Isso dá cerca de 20.000 números por ratinho.

Faz se isso a muitos ratinhos, de idades conhecidas, e fica se com uma tabela. Uma linha por ratinho, uma coluna por gene, e uma última coluna com a idade real.

Ajusta se uma regressão (elastic net ou ridge, porque há 20.000 colunas e poucas linhas) que vai dos genes para a idade. Isso é o relógio. Dá se lhe um ratinho novo e ele devolve uma idade estimada.

O interesse está no desvio. Um ratinho de 22 meses a quem o relógio dá 25 morre em média mais cedo do que um a quem dá 19.

**Nota.** É uma amostra de fígado por ratinho, porque o animal é sacrificado para a tirar. As linhas da tabela são ratinhos diferentes.

**Pergunta ao João.** Na tabela, o que são as linhas, o que são as colunas, e o que é a última coluna?

---

## 3. Os dois relógios (10 min)

**O que dizer.**
No artigo do Tyshkovskiy (Nature 2026) há dois relógios feitos com a mesma tabela de fígados. A única diferença é a última coluna.

**Relógio cronológico.** A última coluna é a idade real do ratinho. Treinado, prediz idade. Se um fármaco fizer o relógio ler 18 num animal de 22 meses, chama se a isso rejuvenescimento de 4 meses.

**Relógio de mortalidade.** A última coluna não é uma propriedade do ratinho. É um número emprestado de outros ratinhos, do mesmo fármaco, que foram deixados viver até morrer. Se o grupo da rapamicina viveu 15 por cento mais que os controlos, todos os fígados de rapamicina levam o mesmo carimbo, menos 15. Os controlos levam zero.

Porque é que fizeram o segundo? Porque o desvio do relógio cronológico correlacionava fracamente com o efeito dos fármacos no tempo de vida. Meter a sobrevivência no rótulo tornou o modelo mais forte.

**Pergunta ao João.** Porque é que não se usa o tempo de vida do próprio ratinho sequenciado? (resposta, porque foi sacrificado aos 22 meses e nunca se sabe quanto viveria)

---

## 4. O problema, e a pergunta da tese (10 min)

**O que dizer.**
O rótulo do relógio de mortalidade veio das curvas de sobrevivência dos fármacos do ITP. Depois o artigo diz que esse relógio prediz quais os fármacos que prolongam a vida. Quais fármacos? Os mesmos cujas curvas estão dentro dos rótulos.

Como cada fármaco deixa uma impressão digital no fígado (certos genes para cima, outros para baixo), o modelo pode aprender um atalho. Reconhece a impressão digital da rapamicina e devolve o carimbo da rapamicina. Nunca precisou de perceber envelhecimento.

Isso é como um aluno que viu a folha de respostas antes do exame.

O que ninguém testou é o que acontece com um fármaco que o modelo nunca viu. E é exatamente isso que um endpoint substituto tem de fazer, dar a resposta para um composto novo. Os autores validaram deixando de fora tecidos, datasets e espécies, mas nunca uma intervenção inteira.

**A pergunta da tese.** Quando o relógio de mortalidade vê um fármaco pela primeira vez, mantém alguma vantagem sobre o relógio cronológico?

**O precedente.** CAST 1989. Dois antiarrítmicos melhoraram o marcador (suprimiram a arritmia) e mais do que duplicaram a mortalidade. Prever não é substituir.

**Pergunta ao João.** Explica me tu o atalho. O que é que o modelo pode aprender em vez de biologia?

---

## 5. O teste (10 min)

**O que dizer.**
Leave one intervention out. Há cerca de 20 fármacos na tabela. Retira se um por inteiro, linhas dos fígados e carimbo de sobrevivência. Treinam se os dois relógios nos outros 19. Depois mostra se lhes o fármaco escondido e vê se o que dizem. Repete se 20 vezes, uma por fármaco.

Os dois relógios fazem exatamente os mesmos folds. Compara se a diferença emparelhada.

**O resultado é um gráfico de dispersão com 20 pontos.** Cada fármaco é um ponto com duas coordenadas.
Coordenada 1, do ficheiro de fígados. Quanto o relógio desceu nesse fármaco em relação aos controlos (por exemplo, menos 3 meses).
Coordenada 2, do ficheiro de sobrevivência. Quanto o tempo de vida subiu (por exemplo, mais 15 por cento).
Se os pontos caem perto de uma reta, o relógio segue o tempo de vida. Se estão espalhados, não segue.

Faz se um gráfico por relógio, com os pontos vindos de folds em que o fármaco nunca foi visto. A tese prevê que a vantagem do relógio de mortalidade desapareça.

**Ponto crítico a transmitir.** Dentro de cada fold, o carimbo de mortalidade tem de ser reconstruído sem a curva de sobrevivência do fármaco escondido. Se o João usar os rótulos publicados pelo tAge, a fuga continua lá e o teste não vale nada. Isto é a primeira coisa que um revisor vai atacar.

**Pergunta ao João.** Se escondes a rapamicina, o que é que tens de tirar do treino? (resposta, os fígados dela E o número que veio da curva de sobrevivência dela)

---

## 6. O resto da tese, em uma frase cada (5 min)

- **Canagliflozina.** Prolonga a vida só em machos, e foi sequenciada nos dois sexos. Se o relógio é substituto válido, a assinatura tem de ser diferente entre sexos. Os autores reportam assinaturas concordantes. Exploratório, um único composto.
- **Substituição ao nível do ensaio.** Quadro de Buyse Molenberghs com o pacote Surrogate em R, sobre a tabela de 20 pontos. Só ao nível do ensaio, porque não há nenhum animal com transcriptoma e tempo de vida.
- **Nulos.** Um preditor aleatório e um modelo sobre o transcriptoma completo, para distinguir um resultado negativo por má qualidade dos dados de um resultado negativo por propriedade do objeto.
- **Relógios de via.** Só se o primário justificar.

---

## 7. O que ele faz esta semana (10 min)

Semana 1, sem código de modelação. Três verificações, todas escritas em `protocol/semana1_portao.md`.

**Descarregar dois ficheiros.**
1. Zenodo 10.5281/zenodo.18763485. A tabela de fígados (170 linhas, genes nas colunas) e os modelos tAge.
2. Mouse Phenome Database, projeto ITP1. Uma linha por ratinho, com fármaco, sexo, idade de início e idade de morte. Sem genes.

Os dois ficheiros têm ratinhos diferentes e só se cruzam pelo nome do fármaco.

**Verificar.**
1. Cada amostra de fígado diz de que fármaco veio? Se só disser "amostra 47", procurar nos metadados do GEO GSE292885 e na tabela suplementar do artigo antes de dar por perdido. Sem isto não há tese.
2. Quantos fármacos têm as duas coisas, fígado sequenciado e curva de sobrevivência? Contar por sexo. Decidir o que conta como "uma intervenção" (composto, composto por dose, composto por idade de início). Esta decisão fixa o N e não muda depois.
3. Esse N chega? Simulação simples com o N real e a correlação verdadeira a variar. Daqui sai a margem do resultado primário.

**Ler.** Tyshkovskiy 2026 (o artigo a ser posto à prova, tem de o saber de cor), Prentice 1989 e CAST 1989 (curtos, dão o argumento).

**Entregáveis para a próxima reunião.** `results/tabela_amostras.csv`, `results/intervencoes.csv`, `protocol/potencia.md` preenchido, e o pré registo esboçado.

---

## 8. Organização (5 min)

- Repositório GitHub `msc-joao-alves`. Ele trabalha em branches, abre pull requests, e cada verificação da semana 1 é um issue.
- Reunião semanal.
- Escrita começa cedo, em paralelo com o resultado primário.

---

## Perguntas que ele pode fazer, e a resposta

**"Porque é que não construímos um relógio nosso?"** Primeiro prova se ou refuta se este. Se passar, o relógio existente aguenta o teste mais duro e há resultado. Se falhar, sabemos porquê, e isso é o que diz o que se pode construir a seguir.

**"Se o resultado for negativo, a tese falha?"** Não. Um resultado negativo bem feito, com pré registo, é a primeira avaliação de substituição na área e publica se. O que não se publica é um intervalo tão largo que não diz nada, e é para evitar isso que existe a semana 1.

**"20 fármacos chegam?"** Não sabemos, e por isso a simulação é a primeira coisa a fazer, antes do código.

**"O que é elastic net?"** Regressão linear com penalização que empurra a maioria dos 20.000 coeficientes para zero. Usa se porque há muito mais colunas do que linhas e um modelo grande memorizava cada fármaco.
