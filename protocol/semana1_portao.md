# Semana 1. Portão de viabilidade (sem código de modelação)

Três perguntas. Todas têm de passar antes de qualquer análise.

## 1. Cada amostra de fígado diz de que fármaco veio?

Abrir a matriz do Zenodo e os metadados do GEO. Para cada uma das 170 amostras, registar fármaco, sexo, idade de início, sítio.
Se os nomes forem só identificadores anónimos, procurar nos metadados do GEO (campo characteristics) e na tabela suplementar do Tyshkovskiy 2026 antes de dar por perdido.

Entregável, `results/tabela_amostras.csv` com uma linha por amostra e as colunas acima.

## 2. Quantos fármacos têm transcriptoma E curva de sobrevivência?

Cruzar a lista de fármacos da tabela acima com o ficheiro do ITP1. Contar, por sexo. Decidir e escrever o que conta como "uma intervenção" (composto? composto x dose? composto x idade de início?). A decisão fixa o N do LOIO e não pode mudar depois.

Entregável, `results/intervencoes.csv` com uma linha por intervenção, número de fígados sequenciados por sexo, e efeito no tempo de vida (mediana e razão de risco contra controlo) por sexo.

## 3. Esse N chega?

Simulação. Gerar N pares (efeito no relógio, efeito no tempo de vida) sob correlação verdadeira 0, 0.3, 0.6, 0.9, com o erro de medição esperado, e ver a largura do intervalo de confiança da diferença emparelhada entre os dois relógios. Daqui sai a margem do resultado primário.

Entregável, `protocol/potencia.md` com a tabela de simulação e a margem escolhida.

## Se passar
Escrever `protocol/pre_registo.md` com hipótese primária, margem, esquema de folds, e o que se faz com cada desfecho possível. Só depois se abre o código.

## Se não passar
Reformular a pergunta nesta semana. Opções a discutir com os orientadores.
