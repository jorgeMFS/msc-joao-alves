# O método, de uma assentada

Ler isto depois do `README.md` e antes de tocar em código. Se alguma coisa aqui não fizer sentido,
é uma pergunta para a reunião, não para contornar.

## 1. A pergunta

Os relógios transcriptómicos servem como **endpoint substituto** para intervenções geroprotetoras?
Concretamente: quando um fármaco **nunca visto pelo modelo** faz o relógio descer, isso prediz que
o fármaco prolonga o tempo de vida?

A pergunta importa porque o tempo de vida de um ratinho custa três anos e muito dinheiro. Se um
relógio o substituísse, o rastreio de fármacos ficava viável. A literatura assume que sim; ninguém
testou com o fármaco fora do treino.

## 2. Os dados, e a restrição que os define

| Fonte | Unidade | O que traz |
|---|---|---|
| Zenodo / GEO | 170 fígados de ratinho | expressão génica, sacrificados aos 22 meses |
| MPD / ITP1 | milhares de ratinhos | fármaco, sexo, sítio, idade de morte |

**São ratinhos diferentes.** Nenhum animal tem transcriptoma *e* tempo de vida. Ligam-se apenas ao
nível do **fármaco**.

Consequência, e é a mais importante do projeto: a substituição **individual** não é estimável. Só
existe substituição **ao nível do ensaio**. Isto vai no pré-registo e na introdução, não na discussão
como limitação descoberta no fim.

## 2b. Os dois relógios, e o atalho

Os dois relógios saem da **mesma tabela de fígados**. A única diferença é a última coluna.

| | Última coluna | O que prevê |
|---|---|---|
| **Relógio cronológico** | idade real do ratinho | idade |
| **Relógio de mortalidade** | **carimbo** do fármaco | risco emprestado |

O carimbo **não é uma propriedade do ratinho sequenciado**. É um número vindo de *outros* ratinhos,
do mesmo fármaco, que foram deixados morrer. Se o grupo da rapamicina viveu 15 % mais que os
controlos, todos os fígados de rapamicina levam o mesmo carimbo. Os controlos levam zero.

Fizeram o segundo relógio porque o desvio do cronológico correlacionava fracamente com o efeito dos
fármacos no tempo de vida. Meter a sobrevivência no rótulo tornou o modelo mais forte.

**E aqui está o problema.** O rótulo veio das curvas de sobrevivência dos fármacos do ITP. Depois
diz-se que o relógio prediz quais os fármacos que prolongam a vida. *Quais fármacos?* Os mesmos
cujas curvas estão dentro dos rótulos.

Como cada fármaco deixa uma **impressão digital** no fígado, certos genes para cima, outros para
baixo, o modelo pode aprender um atalho: reconhece a impressão digital da rapamicina e devolve o
carimbo da rapamicina. Nunca precisou de perceber envelhecimento. É um aluno que viu a folha de
respostas antes do exame.

Os autores validaram deixando de fora tecidos, conjuntos de dados e espécies. **Nunca uma
intervenção inteira.** E é exatamente isso que um endpoint substituto tem de fazer: dar a resposta
para um composto novo.

> **O precedente.** CAST, 1989. Dois antiarrítmicos melhoraram o marcador, suprimiram a arritmia -
> e mais do que duplicaram a mortalidade. Prever não é substituir. (`docs/reading-list.md` §C0)

## 3. O teste central: LOIO

```
para cada intervenção I:
    treino  = todas as amostras EXCETO as de I
    teste   = as amostras de I
    1. reconstruir os rótulos de mortalidade usando SÓ as curvas de sobrevivência do treino
    2. afinar hiperparâmetros DENTRO do treino
    3. treinar o relógio cronológico e o relógio de mortalidade
    4. prever em I, e registar o efeito de I em cada relógio
comparar, emparelhado, os dois relógios ao longo das intervenções
```

Dois pontos onde é fácil enganar-se, e que são o cerne da tese:

**(a) A intervenção inteira sai.** Não amostras da intervenção: a intervenção toda. É o
`GroupKFold` com `intervention` como grupo (`src/clocks/loio.py`).

**(b) Os rótulos são reconstruídos dentro do fold.** Se se usarem os rótulos de mortalidade
publicados com o tAge, a curva de sobrevivência da intervenção retida já entrou na construção
desses rótulos, e a fuga que a tese denuncia continua lá, só que escondida. É por isto que
`build_mortality_labels` existe como função separada e ainda por implementar.

### O resultado, em concreto

**Um gráfico de dispersão com ~20 pontos, um por fármaco.** Cada ponto tem duas coordenadas:

| Eixo | De onde vem | Exemplo |
|---|---|---|
| **x**: efeito no relógio | ficheiro de fígados | o relógio desceu 3 meses face aos controlos |
| **y**: efeito no tempo de vida | ficheiro de sobrevivência | o tempo de vida subiu 15 % |

Se os pontos caem perto de uma reta, o relógio segue o tempo de vida. Se estão espalhados, não segue.

Faz-se **um gráfico por relógio**, com os pontos vindos de folds em que o fármaco nunca foi visto.
A tese prevê que a vantagem do relógio de mortalidade desapareça.

## 4. O que se compara

Resultado primário: a **diferença emparelhada** entre o relógio de mortalidade e o cronológico, na
associação ao nível da intervenção (efeito no relógio vs efeito no tempo de vida), com folds idênticos.

Emparelhada porque as duas quantidades são medidas nas mesmas intervenções, e a variação entre
intervenções é muito maior que a diferença entre relógios. Comparar médias não emparelhadas
desperdiça a maior parte do sinal.

> **Atenção ao tipo de hipótese.** A hipótese primária é de **equivalência com margem
> pré-registada**: que o relógio de mortalidade **não confere** capacidade de generalização
> adicional sobre o cronológico. Não é um teste de diferença. A margem sai da análise de potência da
> semana 1 (`protocol/potencia.md`) e fixa-se **antes** de ver os dados. Um teste de diferença que
> "não rejeita" não é o mesmo que demonstrar equivalência, e a distinção é o que torna um resultado
> negativo publicável.

### Os esquemas de validação, e o que falta

| Esquema | Deixa de fora | Estado |
|---|---|---|
| LOFO | um fold | ✓ feito |
| LOTO | um tecido | ✓ feito |
| LODO | um conjunto de dados | ✓ feito |
| LOSO | uma espécie | ✓ feito |
| **LOIO** | **uma intervenção inteira** | **✗ nunca feito. É esta tese** |

Todos os quatro já corridos **seguram amostras**. Nenhum segura **tratamentos**.

### A previsão pré-registada

| Relógio | r² publicado | Previsão sob LOIO |
|---|---:|---|
| Cronológico (não vê a sobrevivência) | ≈ 0,13 | - |
| Mortalidade (rótulo do próprio tratamento) | ≈ 0,28 | **colapsa para ≈ 0,13** |

Ver `figuras/figura3_esquemas_validacao.png`.

## 5. Os desfechos possíveis, escritos antes

| Se acontecer | Conclui-se |
|---|---|
| O relógio de mortalidade mantém vantagem clara sob LOIO | A abordagem generaliza; substituto plausível ao nível do ensaio |
| A vantagem desaparece sob LOIO mas existia sem LOIO | A vantagem publicada era memorização de intervenções; resultado negativo com valor |
| Nenhum dos dois se associa ao tempo de vida | Os relógios não substituem, e a correlação publicada vem de outro lado |
| O IC é largo de mais para distinguir | O N não chega. **Descobre-se na semana 1**, não no fim |

A última linha é a razão de a análise de potência ser um portão e não um apêndice.

## 6. Ordem de trabalho

1. **Semana 1**: portão: as amostras identificam o fármaco? quantas intervenções têm os dois lados?
   esse N chega? (`protocol/semana1_portao.md`, `protocol/potencia.md`)
2. **Semanas 2-4**: reproduzir **um** valor publicado com os pesos do tAge. Se não se reproduz um
   número conhecido, não se confia em números novos.
3. **Semanas 5-9**: LOIO. Resultado primário.
4. **Semanas 10-14**: tabela de efeitos por intervenção, os dois eixos com erro padrão.
5. **Semanas 15-18**: substituição de nível de ensaio, dimorfismo sexual, nulos.

## 7. Nulos, que não são opcionais

Duas comparações obrigatórias, para saber o que significa o número principal:

- **Baseline aleatório.** Um "relógio" com genes aleatórios, mesmo pipeline. Diz quanto do desempenho
  vem da estrutura e quanto vem do procedimento.
- **Transcriptoma completo regularizado.** Sem seleção de genes. Diz se a seleção do relógio
  acrescenta alguma coisa a uma regressão regularizada honesta.
