# Glossário

Termos do projeto, num só sítio. Ir acrescentando à medida que se lê. Quando um termo aparecer numa
reunião e não for claro, entra aqui no mesmo dia.

## Relógios

- **Relógio de envelhecimento.** Modelo que prevê uma quantidade relacionada com a idade a partir de
  dados moleculares (metilação, expressão génica).
- **Relógio cronológico.** Treinado para prever a **idade** do animal. É o baseline desta tese.
- **Relógio de mortalidade.** Treinado para prever **tempo até à morte** ou risco de morte, não idade.
  A hipótese em teste é que este tem vantagem sobre o cronológico como substituto.
- **tAge.** O relógio transcriptómico publicado com o conjunto de dados do Zenodo. Os seus **pesos
  publicados não podem ser usados** no LOIO, ver "fuga".
- **Carimbo de mortalidade.** O rótulo do relógio de mortalidade. **Não é uma propriedade do
  ratinho sequenciado**: é um número emprestado de *outros* ratinhos do mesmo fármaco que foram
  deixados morrer. Se o grupo da rapamicina viveu 15 % mais, todos os fígados de rapamicina levam
  o mesmo carimbo. Os controlos levam zero.
- **Impressão digital do fármaco.** O padrão de genes que um fármaco deixa no fígado. É o atalho
  possível: o modelo pode reconhecer a impressão digital e devolver o carimbo, sem nunca ter
  percebido envelhecimento.
- **Elastic net / ridge.** Regressão linear com penalização que empurra a maioria dos ~20.000
  coeficientes para zero. Usa-se porque há muito mais colunas (genes) do que linhas (ratinhos), e
  um modelo grande memorizaria cada fármaco.
- **Aceleração de idade.** Resíduo do relógio: idade prevista menos idade real. É a quantidade que
  desce quando uma intervenção "rejuvenesce" o animal.

## Desenho experimental

- **ITP (Interventions Testing Program).** Programa do NIA que testa fármacos em ratinhos
  geneticamente heterogéneos, em três sítios em paralelo, com resultados reportados por sexo.
- **Intervenção.** A unidade de análise desta tese. **A sua definição fixa o N do LOIO** e é decidida
  na semana 1: composto? composto × dose? composto × idade de início? Uma vez no pré-registo, não muda.
- **Efeito no tempo de vida.** Quanto uma intervenção altera a sobrevivência face ao controlo.
  Reportar mediana **e** razão de risco, por sexo.
- **Efeito no relógio.** Quanto uma intervenção baixa a aceleração de idade prevista.

## Validação

- **LOIO (leave one intervention out).** Retirar uma intervenção **inteira** do treino, retreinar,
  e avaliar nessa intervenção nunca vista. É o teste central da tese.
- **LOFO / LOTO / LODO / LOSO.** Os quatro esquemas de validação já corridos pelos autores: deixar
  de fora um fold, um tecido, um conjunto de dados, uma espécie. **Todos seguram amostras.** Nenhum
  segura tratamentos, daí o LOIO.
- **GroupKFold.** A implementação: cada intervenção é um grupo, e um grupo nunca está em treino e
  teste ao mesmo tempo.
- **Fuga (leakage).** Informação do conjunto de teste que entra no treino. Aqui tem duas formas:
  (i) a mesma intervenção em treino e teste; (ii) usar rótulos de mortalidade construídos com a curva
  de sobrevivência da intervenção retida. O `loio.py` tem de eliminar as duas.
- **Rótulo construído dentro do fold.** O rótulo do relógio de mortalidade é reconstruído usando
  **só** as intervenções de treino. Usar os rótulos publicados do tAge reintroduz a fuga.
- **Teste de equivalência.** Demonstrar que duas coisas **não diferem** para além de uma margem Δ
  fixada à partida. Distinto de "não rejeitar diferença zero", que não demonstra nada. A hipótese
  primária desta tese é de equivalência.
- **Margem de equivalência (Δ).** O quanto se aceita como "sem diferença prática". Sai da análise de
  potência da semana 1 e fixa-se **antes** de ver os dados.
- **Diferença emparelhada.** O resultado primário: para cada intervenção, a diferença entre o
  desempenho do relógio de mortalidade e o do cronológico, com folds idênticos.

## Substituição

- **Endpoint substituto (surrogate).** Marcador medido em vez do desfecho que interessa, quando o
  desfecho é lento ou caro. Aqui: o relógio em vez do tempo de vida.
- **Substituição individual.** A associação entre marcador e desfecho **no mesmo indivíduo**.
  **Não é estimável nesta tese**: nenhum ratinho tem transcriptoma e tempo de vida.
- **Substituição ao nível do ensaio.** A associação entre o *efeito da intervenção no marcador* e o
  *efeito da intervenção no desfecho*, através de várias intervenções. É o único nível disponível aqui.
- **Critérios de Prentice.** As condições clássicas para um marcador poder substituir um desfecho.
- **R² de ensaio.** A medida de substituição de nível de ensaio no enquadramento meta-analítico.

## Modelo e dados

- **UM-HET3.** A estirpe de ratinhos geneticamente heterogéneos do ITP. A heterogeneidade é
  deliberada: um efeito que sobrevive a fundos genéticos variados é mais robusto.
- **Score de módulo.** Representação de baixa dimensão, a atividade agregada de um conjunto de
  genes com função comum, usada em vez dos ~20.000 genes individuais.
- **Relógio de via.** Relógio construído sobre um módulo específico (inflamatório, mitocondrial,
  metabólico), para testar se a substituição é específica de mecanismo.
- **Teste de permutação.** Calibrar a significância baralhando os rótulos. Aqui tem de **respeitar a
  estrutura de dependência**: baralhar ao nível da intervenção, não da amostra.

## Estatística

- **Razão de risco (hazard ratio).** Efeito de uma intervenção na taxa instantânea de morte.
- **Kaplan-Meier.** Estimador não-paramétrico da curva de sobrevivência.
- **Análise de potência.** Simular antes de analisar, para saber se o N disponível consegue responder
  à pergunta. Entregável da semana 1 (`protocol/potencia.md`).
- **Pré-registo.** Escrever hipótese, margem e regra de decisão **antes** de ver os dados.
  `protocol/pre_registo.md`.
